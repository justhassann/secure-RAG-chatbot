const API_BASE = "http://localhost:8000";

// Check if user is logged in
let currentUser = JSON.parse(localStorage.getItem("currentUser"));
if (!currentUser) {
  window.location.href = "/static/login.html";
}

// DOM Elements
const viewTitle = document.getElementById("viewTitle");
const userAvatar = document.getElementById("userAvatar");
const userName = document.getElementById("userName");
const userRole = document.getElementById("userRole");
const statusIndicator = document.getElementById("statusIndicator");
const statusText = document.getElementById("statusText");
const modelSelect = document.getElementById("modelSelect");
const logoutBtn = document.getElementById("logoutBtn");

// Views
const chatView = document.getElementById("chatView");
const profileView = document.getElementById("profileView");
const adminView = document.getElementById("adminView");

// Chat elements
const messagesEl = document.getElementById("messages");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const scopeBadges = document.getElementById("scopeBadges");

// Navigation
const navItems = document.querySelectorAll(".nav-item");
const adminNavItem = document.querySelector('.nav-item[data-view="admin"]');

let sending = false;

// Initialize app
function initApp() {
  // Set user info in top bar
  userAvatar.textContent = currentUser.avatar;
  userName.textContent = currentUser.fullName;
  userRole.textContent = currentUser.role;

  // Show admin link for privileged roles
  if (["SysAdmin", "Auditor", "Executive"].includes(currentUser.role)) {
    adminNavItem.classList.remove("hidden");
  }

  // Display AI scopes in chat header
  renderScopes();

  // Load profile data
  loadProfileData();

  // Check backend health
  checkHealth();

  // Set up navigation
  navItems.forEach(item => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      const view = item.dataset.view;
      switchView(view);
    });
  });

  // Logout
  logoutBtn.addEventListener("click", () => {
    localStorage.removeItem("currentUser");
    window.location.href = "/static/login.html";
  });

  // Chat functionality
  sendBtn.addEventListener("click", sendMessage);
  userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
}

function switchView(viewName) {
  // Update nav
  navItems.forEach(item => {
    if (item.dataset.view === viewName) {
      item.classList.add("active");
    } else {
      item.classList.remove("active");
    }
  });

  // Update views
  chatView.classList.remove("active");
  profileView.classList.remove("active");
  adminView.classList.remove("active");

  if (viewName === "chat") {
    chatView.classList.add("active");
    viewTitle.textContent = "AI Assistant";
  } else if (viewName === "profile") {
    profileView.classList.add("active");
    viewTitle.textContent = "My Profile";
  } else if (viewName === "admin") {
    adminView.classList.add("active");
    viewTitle.textContent = "Admin Panel";
  }
}

function renderScopes() {
  scopeBadges.innerHTML = "";
  currentUser.aiScopes.forEach(scope => {
    const badge = document.createElement("span");
    badge.className = "scope-badge";
    badge.textContent = scope;
    scopeBadges.appendChild(badge);
  });
}

async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error("Health check failed");
    statusIndicator.classList.add("online");
    statusIndicator.classList.remove("offline");
    statusText.textContent = "Online";
  } catch (e) {
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

  // Show user message
  appendMessage(text, "user");
  userInput.value = "";

  setSending(true);

  // Create empty bot message for streaming
  const botDiv = document.createElement("div");
  botDiv.classList.add("message", "bot");
  messagesEl.appendChild(botDiv);

  try {
    const res = await fetch(`${API_BASE}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-User-Role": currentUser.role,
        "X-User-Department": currentUser.department
      },
      body: JSON.stringify({ query: text, model })
    });

    if (!res.ok) {
      const errorText = await res.text();
      botDiv.textContent = `Error: ${res.status} ${errorText}`;
      return;
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n\n");
      buffer = lines.pop();

      for (const line of lines) {
        if (line.startsWith("data: ")) {
          const data = JSON.parse(line.slice(6));
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
    botDiv.textContent = "Error talking to backend: " + err.message;
  } finally {
    setSending(false);
  }
}

function loadProfileData() {
  // Profile header
  document.getElementById("profileAvatar").textContent = currentUser.avatar;
  document.getElementById("profileName").textContent = currentUser.fullName;
  document.getElementById("profileTitle").textContent = currentUser.jobTitle;

  // Profile details
  document.getElementById("profileRoleBadge").textContent = currentUser.role;
  document.getElementById("profileDeptBadge").textContent = currentUser.department;
  document.getElementById("profileEmail").textContent = currentUser.email;
  document.getElementById("profileLocation").textContent = currentUser.location;

  // AI Access scopes
  const profileScopes = document.getElementById("profileScopes");
  profileScopes.innerHTML = "";
  currentUser.aiScopes.forEach(scope => {
    const badge = document.createElement("span");
    badge.className = "scope-badge";
    badge.textContent = scope;
    profileScopes.appendChild(badge);
  });

  // Permissions
  const canViewLogs = document.getElementById("profileCanViewLogs");
  canViewLogs.textContent = currentUser.canViewLogs ? "Yes" : "No";
  canViewLogs.className = currentUser.canViewLogs ? "permission-badge yes" : "permission-badge no";

  const canManageUsers = document.getElementById("profileCanManageUsers");
  canManageUsers.textContent = currentUser.canManageUsers ? "Yes" : "No";
  canManageUsers.className = currentUser.canManageUsers ? "permission-badge yes" : "permission-badge no";

  const canManageKB = document.getElementById("profileCanManageKB");
  canManageKB.textContent = currentUser.canManageKB ? "Yes" : "No";
  canManageKB.className = currentUser.canManageKB ? "permission-badge yes" : "permission-badge no";
}

// Initialize on load
initApp();
