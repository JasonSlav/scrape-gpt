const wrapper = document.querySelector(".wrapper");
const registerLink = document.querySelector(".register-link");
const loginLink = document.querySelector(".login-link");

if (registerLink && wrapper && loginLink) {

  registerLink.onclick = () => {
    wrapper.classList.add("active");
  };
  loginLink.onclick = () => {
    wrapper.classList.remove("active");
  };
}

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
//share link
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", async function (event) {
      event.preventDefault(); // Mencegah reload halaman

      const urlInput = document.getElementById("url").value;
      const description = document.getElementById("description").value;

      // Kirim data ke backend
      try {
          const response = await fetch("/run", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json"
              },
              body: JSON.stringify({
                  query: urlInput, // Sesuaikan dengan backend
                  description: description // Bisa disesuaikan jika diperlukan
              })
          });

          const result = await response.json();
          if (response.ok) {
              alert("Scraping berhasil! Data: " + JSON.stringify(result.data));
          } else {
              alert("Gagal: " + result.error);
          }
      } catch (error) {
          console.error("Error:", error);
          alert("Terjadi kesalahan saat mengirim permintaan.");
      }
  });
});