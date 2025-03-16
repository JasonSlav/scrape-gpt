// import navbar
document.addEventListener("DOMContentLoaded", function () {
    fetch("/navbar")
        .then((response) => {
            if (!response.ok) {
                throw new Error("File tidak ditemukan");
            }
            return response.text();
        })
        .then((data) => {
            document.getElementById("navbar-container").innerHTML = data;
            selectNavbar();
            hideNavbar();
        })
        .catch((error) => console.error("Error:", error));
});

// select navbar
function selectNavbar() {
    if (document.getElementById("home")) {
        const homeNav = document.getElementById("home-nav");
        homeNav.classList.toggle("rounded-md");
        homeNav.classList.toggle("text-white");
        homeNav.classList.toggle("bg-custom/20");
    } if (document.getElementById("history")) {
        const historyNav = document.getElementById("history-nav");
        historyNav.classList.toggle("rounded-md");
        historyNav.classList.toggle("text-white");
        historyNav.classList.toggle("bg-custom/20");
    } if (document.getElementById("chat")) {
        const chatNav = document.getElementById("chat-nav");
        chatNav.classList.toggle("rounded-md");
        chatNav.classList.toggle("text-white");
        chatNav.classList.toggle("bg-custom/20");
    }
}


// hide navbar 
function hideNavbar() {
    const hideSidebar = document.getElementById("hide-sidebar");
    const sideBar = document.getElementById("sidebar");
    const menuToggle = document.getElementById("menu-toggle");
    const promptList = document.getElementById("prompt-list");
    const titleChat = document.getElementById("title-chat");

    if ((hideSidebar && sideBar)) {
        hideSidebar.addEventListener("click", function () {
            sideBar.classList.toggle("-translate-x-full");
            sideBar.classList.toggle("fixed");
            menuToggle.classList.toggle("hidden");
        });
        if (menuToggle) {
            menuToggle.addEventListener("click", function () {
                sideBar.classList.toggle("-translate-x-full");
                sideBar.classList.toggle("fixed");
                menuToggle.classList.toggle("hidden");
            });
        }
    }


    if (promptList && titleChat) {
        promptList.addEventListener("click", function () {
            titleChat.classList.toggle("hidden");
        });
    }
}


// dropdown profile
document.getElementById("dropdownButton").addEventListener("click", function () {
    document.getElementById("dropdownMenu").classList.toggle("hidden");
});

document.addEventListener("click", function (event) {
    const dropdown = document.getElementById("dropdownMenu");
    const button = document.getElementById("dropdownButton");
    if (!button.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.classList.add("hidden");
    }
});