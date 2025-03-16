document.addEventListener("DOMContentLoaded", function () {
    // LOGIN
    document.querySelector(".form-box.login form").addEventListener("submit", async function (event) {
        event.preventDefault();

        let username = document.getElementById("loginUsername").value;
        let password = document.getElementById("loginPassword").value;

        let formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        let response = await fetch("/auth/login", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData
        });

        let result = await response.json();
        if (response.ok) {
            alert(result.message);
            localStorage.setItem("token", "logged-in");
            window.location.href = "/home";
        } else {
            alert(result.error);
        }
    });

    // REGISTER
    document.querySelector(".form-box.register form").addEventListener("submit", async function (event) {
        event.preventDefault();

        let username = document.querySelector(".form-box.register input[type='text']").value;
        let password = document.getElementById("signupPassword").value;

        let formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        let response = await fetch("/auth/register", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData
        });

        let result = await response.json();
        if (response.ok) {
            alert(result.message);
            window.location.href = "/home";
        } else {
            alert(result.error);
        }
    });

    // LOGOUT
    document.getElementById("logoutButton")?.addEventListener("click", async function () {
        let response = await fetch("/auth/logout", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        });

        let result = await response.json();
        if (response.ok) {
            alert(result.message);
            localStorage.removeItem("token");
            window.location.href = "/index";
        } else {
            alert(result.error);
        }
    });
});