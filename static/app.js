const API_BASE = window.location.origin;

const accessToken = localStorage.getItem("accessToken");
if (!accessToken) {
  window.location.href = "/static/login.html";
}

function handleUnauthorized() {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("currentUsername");
  window.location.href = "/static/login.html";
}

function decodeJwt(token) {
  try {
    const payload = token.split(".")[1];
    return JSON.parse(atob(payload));
  } catch {
    return {};
  }
}

const decodedToken = decodeJwt(accessToken);
const storedUsername = localStorage.getItem("currentUsername");
const username = storedUsername || decodedToken.sub || "user";
const profile =
  (typeof EMPLOYEES !== "undefined" &&
    EMPLOYEES.find((emp) => emp.username === username)) || {
    username,
    fullName: username,
    role: decodedToken.role || "Staff",
    department: "general",
    avatar: username.charAt(0).toUpperCase(),
    aiScopes: [],
    email: "",
    location: "",
    jobTitle: "",
    canViewLogs: false,
    canManageUsers: false,
    canManageKB: false,
  };

// DOM references
const messagesEl = document.getElementById("messages");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const modelSelect = document.getElementById("modelSelect");
const statusIndicator = document.getElementById("statusIndicator");
const statusText = document.getElementById("statusText");
const navItems = document.querySelectorAll(".nav-item");
const viewTitle = document.getElementById("viewTitle");
const chatView = document.getElementById("chatView");
const profileView = document.getElementById("profileView");
const adminView = document.getElementById("adminView");
const logoutBtn = document.getElementById("logoutBtn");
const userAvatar = document.getElementById("userAvatar");
const userName = document.getElementById("userName");
const userRole = document.getElementById("userRole");
const scopeBadges = document.getElementById("scopeBadges");
const profileAvatar = document.getElementById("profileAvatar");
const profileName = document.getElementById("profileName");
const profileTitle = document.getElementById("profileTitle");
const profileRoleBadge = document.getElementById("profileRoleBadge");
const profileDeptBadge = document.getElementById("profileDeptBadge");
const profileEmail = document.getElementById("profileEmail");
const profileLocation = document.getElementById("profileLocation");
const profileScopes = document.getElementById("profileScopes");
const canViewLogsEl = document.getElementById("profileCanViewLogs");
const canManageUsersEl = document.getElementById("profileCanManageUsers");
const canManageKBEl = document.getElementById("profileCanManageKB");
const adminNavItem = document.querySelector('.nav-item[data-view="admin"]');

// Security modal elements
const securityBtn = document.getElementById("securityBtn");
const securityModal = document.getElementById("securityModal");
const modalBackdrop = document.getElementById("modalBackdrop");
const closeSecurityModalBtn = document.getElementById("closeSecurityModal");
const start2faBtn = document.getElementById("start2faBtn");
const twofaSetupContainer = document.getElementById("twofaSetupContainer");
const twofaQrImage = document.getElementById("twofaQrImage");
const twofaVerifyCode = document.getElementById("twofaVerifyCode");
const verify2faBtn = document.getElementById("verify2faBtn");
const twofaFeedback = document.getElementById("twofaFeedback");
const twofaStatus = document.getElementById("twofaStatus");

let sending = false;

function authHeaders(extra = {}) {
  return {
    ...extra,
    Authorization: `Bearer ${accessToken}`,
  };
}

async function apiFetch(path, options = {}) {
  const opts = { ...options };
  opts.headers = authHeaders(options.headers || {});

  const response = await fetch(`${API_BASE}${path}`, opts);
  if (response.status === 401) {
    handleUnauthorized();
    return Promise.reject(new Error("Session expired"));
  }
  return response;
}

function initUserUI() {
  userAvatar.textContent = profile.avatar || profile.fullName.charAt(0);
  userName.textContent = profile.fullName || profile.username;
  userRole.textContent = profile.role;

  if (["SysAdmin", "Auditor", "Executive"].includes(profile.role)) {
    adminNavItem.classList.remove("hidden");
  }

  scopeBadges.innerHTML = "";
  (profile.aiScopes || []).forEach((scope) => {
    const span = document.createElement("span");
    span.className = "scope-badge";
    span.textContent = scope;
    scopeBadges.appendChild(span);
  });

  profileAvatar.textContent = profile.avatar || profile.fullName.charAt(0);
  profileName.textContent = profile.fullName || profile.username;
  profileTitle.textContent = profile.jobTitle || "Team Member";
  profileRoleBadge.textContent = profile.role;
  profileDeptBadge.textContent = profile.department;
  profileEmail.textContent = profile.email || "N/A";
  profileLocation.textContent = profile.location || "Remote";

  profileScopes.innerHTML = "";
  (profile.aiScopes || []).forEach((scope) => {
    const badge = document.createElement("span");
    badge.className = "scope-badge";
    badge.textContent = scope;
    profileScopes.appendChild(badge);
  });

  canViewLogsEl.textContent = profile.canViewLogs ? "Yes" : "No";
  canViewLogsEl.className = profile.canViewLogs ? "permission-badge yes" : "permission-badge no";
  canManageUsersEl.textContent = profile.canManageUsers ? "Yes" : "No";
  canManageUsersEl.className = profile.canManageUsers ? "permission-badge yes" : "permission-badge no";
  canManageKBEl.textContent = profile.canManageKB ? "Yes" : "No";
  canManageKBEl.className = profile.canManageKB ? "permission-badge yes" : "permission-badge no";
}

async function checkHealth() {
  try {
    const response = await fetch(`${API_BASE}/health`);
    if (!response.ok) throw new Error();
    statusIndicator.classList.add("online");
    statusIndicator.classList.remove("offline");
    statusText.textContent = "Online";
  } catch {
    statusIndicator.classList.add("offline");
    statusIndicator.classList.remove("online");
    statusText.textContent = "Offline";
  }
}

function appendMessage(text, type = "bot") {
  const div = document.createElement("div");
  div.classList.add("message", type);
  div.textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return div;
}

function setSending(isSending) {
  sending = isSending;
  sendBtn.disabled = isSending;
  sendBtn.textContent = isSending ? "Sending..." : "Send";
}

async function sendMessage() {
  const text = userInput.value.trim();
  if (!text || sending) return;

  const model = modelSelect.value;
  appendMessage(text, "user");
  userInput.value = "";
  setSending(true);

  const botDiv = appendMessage("", "bot");

  try {
    const response = await fetch(`${API_BASE}/api/chat`, {
      method: "POST",
      headers: authHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({ query: text, model }),
    });

    if (response.status === 401) {
      handleUnauthorized();
      return;
    }

    if (!response.ok) {
      botDiv.textContent = `Error: ${response.status}`;
      return;
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const segments = buffer.split("\n\n");
      buffer = segments.pop();

      for (const segment of segments) {
        if (segment.startsWith("data: ")) {
          const data = JSON.parse(segment.slice(6));
          if (data.error) {
            botDiv.textContent = `Error: ${data.error}`;
          } else if (data.content) {
            botDiv.textContent += data.content;
            messagesEl.scrollTop = messagesEl.scrollHeight;
          }
        }
      }
    }
  } catch (err) {
    botDiv.textContent = `Error: ${err.message}`;
  } finally {
    setSending(false);
  }
}

function switchView(view) {
  navItems.forEach((item) => {
    item.classList.toggle("active", item.dataset.view === view);
  });

  chatView.classList.remove("active");
  profileView.classList.remove("active");
  adminView.classList.remove("active");

  if (view === "chat") {
    chatView.classList.add("active");
    viewTitle.textContent = "AI Assistant";
  } else if (view === "profile") {
    profileView.classList.add("active");
    viewTitle.textContent = "My Profile";
  } else if (view === "admin") {
    adminView.classList.add("active");
    viewTitle.textContent = "Admin Panel";
  }
}

function showSecurityModal() {
  securityModal.classList.remove("hidden");
  modalBackdrop.classList.remove("hidden");
  twofaSetupContainer.classList.add("hidden");
  twofaFeedback.classList.add("hidden");
  twofaVerifyCode.value = "";
}

function hideSecurityModal() {
  securityModal.classList.add("hidden");
  modalBackdrop.classList.add("hidden");
}

start2faBtn.addEventListener("click", async () => {
  twofaFeedback.classList.add("hidden");
  twofaFeedback.classList.remove("success");
  try {
    const response = await apiFetch("/api/2fa/setup", { method: "POST" });
    const data = await response.json();
    twofaQrImage.src = data.qr_code;
    twofaSetupContainer.classList.remove("hidden");
    twofaStatus.textContent = "Scan the QR code and verify to enable 2FA.";
  } catch (err) {
    twofaFeedback.textContent = err.message || "Unable to start setup.";
    twofaFeedback.classList.remove("hidden");
  }
});

verify2faBtn.addEventListener("click", async () => {
  const code = twofaVerifyCode.value.trim();
  if (code.length !== 6) {
    twofaFeedback.textContent = "Enter the 6-digit code from your authenticator app.";
    twofaFeedback.classList.remove("hidden");
    twofaFeedback.classList.remove("success");
    return;
  }

  try {
    const response = await apiFetch("/api/2fa/enable", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code }),
    });
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || "Unable to enable 2FA.");
    }
    twofaFeedback.textContent = "Two-factor authentication enabled!";
    twofaFeedback.classList.remove("hidden");
    twofaFeedback.classList.add("success");
    twofaStatus.textContent = "2FA is enabled.";
    twofaSetupContainer.classList.add("hidden");
  } catch (err) {
    twofaFeedback.textContent = err.message;
    twofaFeedback.classList.remove("hidden");
    twofaFeedback.classList.remove("success");
  }
});

securityBtn.addEventListener("click", showSecurityModal);
closeSecurityModalBtn.addEventListener("click", hideSecurityModal);
modalBackdrop.addEventListener("click", hideSecurityModal);

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

navItems.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    switchView(item.dataset.view);
  });
});

logoutBtn.addEventListener("click", () => {
  handleUnauthorized();
});

initUserUI();
switchView("chat");
checkHealth();

