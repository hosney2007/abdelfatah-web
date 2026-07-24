window.addEventListener("scroll", function () {
    const navbar = document.getElementById("navbar");
    if (window.scrollY > 50){
        navbar.classList.add("scrolled");
    }else{
        navbar.classList.remove("scrolled")
    }

});

//study mode
const offline = document.querySelector('input[value="offline"]');
const online = document.querySelector('input[value="online"]');
//branch box
const branchBox = document.getElementById("branch-box");
const schadulebox = document.getElementById("schadule-box");
if (branchBox && schadulebox && online && offline) {

    branchBox.style.display = "none";
    schadulebox.style.display = "none";
    //oflin
    offline.addEventListener("change",function(){
        branchBox.style.display = "flex"
        schadulebox.style.display = "none"

    });

    online.addEventListener("change",function(){
        branchBox.style.display = "none"
        schadulebox.style.display = "flex"

    });

}
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



AOS.init({
    duration: 900,
    once: true,
    easing:"ease-in-out",
    offset: 100
})