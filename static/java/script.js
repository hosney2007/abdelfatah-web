console.log("SCRIPT LOADED")



const navbar = document.querySelector(".navbar");
if (document.body.scrollHeight <= window.innerHeight){
    navbar.classList.add("scrolled");
}
window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 50){
        navbar.classList.add("scrolled");
    }else{
        navbar.classList.remove("scrolled")
    }

});

const counters = document.querySelectorAll(".counter");
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry =>{
        if (entry.isIntersecting){

            const counter = entry.target;
            const target = +counter.dataset.target;
            let current = 0;
            const increment = target /100;
            const updatecounter = () =>{
                if (current < target) {
                    current += increment;
                    counter.innerText = Math.ceil(current);
                    requestAnimationFrame(updatecounter);

                } else {
                    counter.innerText = target + "+"
                }
            };
            updatecounter();
            counterObserver.unobserve(counter);


        }
    });
});
counters.forEach( counter => counterObserver.observe(counter));


//hamburger menu
const hamburger = document.getElementById("hamburger");
const navlinks = document.getElementById("nav-links");
hamburger.addEventListener("click", function(){
    navlinks.classList.toggle("active");
    if (navlinks.classList.contains("active")) {
        hamburger.innerHTML ="×";
        } else{
            hamburger.innerHTML ="≡";
    }
});





AOS.init({
    duration: 900,
    once: true,
    easing:"ease-in-out",
    offset: 100
})











// ===============================
// Booking options
// ===============================

const exam = document.getElementById("exam");

const offline = document.querySelector('input[value="offline"]');
const online = document.querySelector('input[value="online"]');

const branchBox = document.getElementById("branch-box");
const branch = document.getElementById("branch");

const scheduleBox = document.getElementById("schedule-box");
const schedule = document.getElementById("schedule");


// ===============================
// Load available groups
// ===============================

async function loadSchedules() {
    console.log("loadSchedules");

    const examValue = exam.value;

    const modeValue = document.querySelector(
        'input[name="mode"]:checked'
    )?.value;

    const branchValue = branch.value;


    // لو لسه مفيش Exam أو Mode
    if (!examValue || !modeValue) {

        scheduleBox.style.display = "none";

        schedule.innerHTML = `
            <option value="">Choose Group</option>
        `;

        return;
    }


    // ===============================
    // ONLINE
    // ===============================

    if (modeValue === "online") {

        branchBox.style.display = "none";

    }


    // ===============================
    // OFFLINE
    // ===============================

    if (modeValue === "offline") {

        branchBox.style.display = "flex";

        // لازم يختار الفرع
        if (!branchValue) {

            scheduleBox.style.display = "none";

            schedule.innerHTML = `
                <option value="">Choose Group</option>
            `;

            return;
        }

    }


    // ===============================
    // Get groups from Flask
    // ===============================

    let url =
        `/booking/schedules?course_id=${examValue}&mode=${modeValue}`;


    if (modeValue === "offline") {

        url += `&branch_id=${branchValue}`;

    }


    const response = await fetch(url);
    console.log(response);

    const schedules = await response.json();
    console.log(schedules);


    // نمسح القديم
    schedule.innerHTML = `
        <option value="">Choose Group</option>
    `;


    // نعرض الجروبات
    schedules.forEach(item => {

        const option = document.createElement("option");

        option.value = item.id;

        option.textContent = item.text
  
        schedule.appendChild(option);

    });


    scheduleBox.style.display = "flex";
}


// ===============================
// Events
// ===============================

exam.addEventListener("change", loadSchedules);

offline.addEventListener("change", loadSchedules);

online.addEventListener("change", loadSchedules);

branch.addEventListener("change", loadSchedules);



document.querySelectorAll(".toast").forEach(function(toast){

    setTimeout(function(){

        toast.style.opacity="0";

        toast.style.transform="translateX(120%)";

        setTimeout(function(){

            toast.remove();

        },300);

    },5000);

});

document.querySelectorAll(".close-toast").forEach(function(btn){

    btn.onclick=function(){

        this.parentElement.remove();

    }

});
