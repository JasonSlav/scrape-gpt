document.addEventListener("DOMContentLoaded", async function () {

    const navbarContainer = document.getElementById("navbar-container");
    if (!navbarContainer) {
        console.error("Elemen #navbar-container tidak ditemukan!");
        return;
    }

    try {
        const navbarResponse = await fetch("/navbar");
        if (!navbarResponse.ok) {
            throw new Error("Gagal memuat navbar. Status: " + navbarResponse.status);
        }

        const navbarHTML = await navbarResponse.text();
        navbarContainer.innerHTML = navbarHTML;

        setTimeout(() => {
            selectNavbar();
            hideNavbar();
        }, 500);

    } catch (error) {
        console.error("Error loading navbar:", error);
    }

    // Load conversations
    const titleChatContainer = document.getElementById("title-chat");
    if (!titleChatContainer) {
        console.error("Element title-chat tidak ditemukan!");
        return;
    }

    try {
        const response = await fetch("/scrape/conversations");
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const conversations = await response.json();

        if (conversations.length === 0) {
            titleChatContainer.innerHTML = `<div class="text-gray-400 px-2 py-2">Belum ada percakapan.</div>`;
            return;
        }

        titleChatContainer.innerHTML = "";
        titleChatContainer.classList.remove("hidden");

        conversations.forEach(conv => {
            const listItem = document.createElement("li");
            listItem.innerHTML = `<a href="/chat/${conv.id}" class="group flex items-center px-2 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 rounded-button">${conv.description || "Tanpa Judul"}</a>`;
            titleChatContainer.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error fetching titles:", error);
        titleChatContainer.innerHTML = `<li class="text-red-400 px-2 py-2">Gagal memuat data.</li>`;
    }
});

function selectNavbar() {
    const path = window.location.pathname;
    document.querySelectorAll("nav a").forEach(el => el.classList.remove("bg-gray-700"));
    const selectedNav = document.getElementById(`${path.includes("home") ? "home" : path.includes("history") ? "history" : "chat"}-nav`);
    if (selectedNav) {
        selectedNav.classList.add("bg-gray-700");
    }
}

function hideNavbar() {
    const hideSidebar = document.getElementById("hide-sidebar");
    const sideBar = document.getElementById("sidebar");
    const menuToggle = document.getElementById("menu-toggle");
    const promptList = document.getElementById("prompt-list");
    const titleChat = document.getElementById("title-chat");

    if (hideSidebar && sideBar) {
        hideSidebar.addEventListener("click", () => {
            sideBar.classList.toggle("-translate-x-full");
            sideBar.classList.toggle("fixed");
            menuToggle.classList.toggle("hidden");
        });
    }
    
    if (menuToggle) {
        menuToggle.addEventListener("click", () => {
            sideBar.classList.toggle("-translate-x-full");
            sideBar.classList.toggle("fixed");
            menuToggle.classList.toggle("hidden");
        });
    }

    if (promptList && titleChat) {
        promptList.addEventListener("click", () => {
            titleChat.classList.toggle("hidden");
        });
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.getElementById("dropdownButton");
    const dropdownMenu = document.getElementById("dropdownMenu");
    
    if (dropdownButton && dropdownMenu) {
        dropdownButton.addEventListener("click", function () {
            dropdownMenu.classList.toggle("hidden");
        });

        document.addEventListener("click", function (event) {
            if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add("hidden");
            }
        });
    }
});