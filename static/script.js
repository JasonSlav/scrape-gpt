const wrapper = document.querySelector(".wrapper");
const registerLink = document.querySelector(".register-link");
const loginLink = document.querySelector(".login-link");
//login register
if (registerLink && wrapper && loginLink) {

  registerLink.onclick = () => {
    wrapper.classList.add("active");
  };
  loginLink.onclick = () => {
    wrapper.classList.remove("active");
  };
}
//toggle password
document.querySelectorAll(".toggle-password").forEach((icon) => {
  icon.addEventListener("click", function () {
    const passwordInput = document.getElementById(this.dataset.target);
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      this.classList.replace("bxs-lock-alt", "bxs-lock-open-alt");
    } else {
      passwordInput.type = "password";
      this.classList.replace("bxs-lock-open-alt", "bxs-lock-alt");
    }
  });
});