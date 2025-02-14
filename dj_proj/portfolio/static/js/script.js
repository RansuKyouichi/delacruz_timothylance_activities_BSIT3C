var typed = new Typed(".text-type", {
    strings: ["I'm a Web Developer?", "I'm a Programmer?", "I'm a Frontend Developer?"],
    typeSpeed: 50,
    backSpeed: 50,
    backDelay: 1000,
    loop: true
});

const tabs = document.querySelectorAll('.tab-btn');
const all_content = document.querySelectorAll('.contents');

// Set the initial active tab and content
tabs[0].classList.add('active');
all_content[0].classList.add('active');

tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        // Remove 'active' class from all tabs and contents
        tabs.forEach(tab => {
            tab.classList.remove('active');
        });
        all_content.forEach(content => {
            content.classList.remove('active');
        });

        // Add 'active' class to the clicked tab and corresponding content
        tab.classList.add('active');
        all_content[index].classList.add('active');
    });
});

const infoTabs = document.querySelectorAll('.info-tab');
const hobbiesSkillsContent = document.querySelectorAll('.hobbies, .skills');

infoTabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        infoTabs.forEach(btn => btn.classList.remove('active'));
        tab.classList.add('active');

        hobbiesSkillsContent.forEach(content => content.classList.remove('active'));
        hobbiesSkillsContent[index].classList.add('active');
    });
});

const body = document.querySelector("body"),
    modeToggle = body.querySelector(".mode-toggle"),
    modeIcon = body.querySelector(".mode i"),
    modeText = body.querySelector(".link-name");

let getMode = localStorage.getItem("mode");

if (getMode && getMode === "light") {
    body.classList.add("light");
    modeIcon.classList.replace("fa-moon", "fa-sun");
    modeText.textContent = "Light Mode";
} else {
    modeIcon.classList.replace("fa-sun", "fa-moon");
    modeText.textContent = "Dark Mode";
}

modeToggle.addEventListener("click", () => {
    body.classList.toggle("light");
    if (body.classList.contains("light")) {
        modeIcon.classList.replace("fa-moon", "fa-sun");
        modeText.textContent = "Light Mode";
        localStorage.setItem("mode", "light");
    } else {
        modeIcon.classList.replace("fa-sun", "fa-moon");
        modeText.textContent = "Dark Mode";
        localStorage.setItem("mode", "dark");
    }
});

