const API_BASE = window.location.origin;

const loginForm = document.getElementById("loginForm");
const errorBanner = document.getElementById("errorBanner");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const totpInput = document.getElementById("totpCode");
const usernameGroup = document.getElementById("usernameGroup");
const passwordGroup = document.getElementById("passwordGroup");
const totpGroup = document.getElementById("totpGroup");
const submitBtn = document.getElementById("submitBtn");
const backBtn = document.getElementById("backToLoginBtn");

let loginPhase = "credentials";
let preAuthToken = null;
let pendingUsername = null;

function showError(message) {
  errorBanner.textContent = message;
  errorBanner.classList.remove("hidden");
}

function hideError() {
  errorBanner.classList.add("hidden");
}

function setPhase(phase) {
  loginPhase = phase;
  if (phase === "credentials") {
    usernameGroup.classList.remove("hidden");
    passwordGroup.classList.remove("hidden");
    totpGroup.classList.add("hidden");
    submitBtn.textContent = "Sign In";
    backBtn.classList.add("hidden");
    totpInput.value = "";
    preAuthToken = null;
  } else {
    usernameGroup.classList.add("hidden");
    passwordGroup.classList.add("hidden");
    totpGroup.classList.remove("hidden");
    submitBtn.textContent = "Verify Code";
    backBtn.classList.remove("hidden");
  }
}

function storeSession(token, username) {
  localStorage.setItem("accessToken", token);
  localStorage.setItem("currentUsername", username);
}

function redirectToApp() {
  window.location.href = "/static/app.html";
}

async function requestToken(username, password) {
  const body = new URLSearchParams();
  body.append("username", username);
  body.append("password", password);

  const response = await fetch(`${API_BASE}/api/token`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Login failed.");
  }

  return response.json();
}

async function verifyTwoFactor(code) {
  const response = await fetch(`${API_BASE}/api/2fa/verify`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pre_auth_token: preAuthToken, code })
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Invalid 2FA code.");
  }

  return response.json();
}

loginForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  hideError();

  try {
    if (loginPhase === "credentials") {
      const username = usernameInput.value.trim();
      const password = passwordInput.value;

      if (!username || !password) {
        showError("Please provide your username and password.");
        return;
      }

      const result = await requestToken(username, password);
      pendingUsername = username;

      if (result.access_token) {
        storeSession(result.access_token, username);
        redirectToApp();
        return;
      }

      if (result.state === "2fa_required") {
        preAuthToken = result.pre_auth_token;
        setPhase("2fa");
        showError("Two-factor authentication required. Enter the code from your authenticator app.");
        return;
      }

      showError("Unexpected response from server.");
    } else {
      const code = totpInput.value.trim();
      if (!code || code.length !== 6) {
        showError("Enter the 6-digit authentication code.");
        return;
      }

      const result = await verifyTwoFactor(code);
      storeSession(result.access_token, pendingUsername || "user");
      redirectToApp();
    }
  } catch (err) {
    showError(err.message);
  }
});

backBtn.addEventListener("click", () => {
  setPhase("credentials");
});

// Auto-redirect if already authenticated
const existingToken = localStorage.getItem("accessToken");
if (existingToken) {
  redirectToApp();
} else {
  setPhase("credentials");
}
