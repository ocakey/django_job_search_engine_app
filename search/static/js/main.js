/*DROP DOWN MENU FUNCTION*/
const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");
const optionsList = document.querySelectorAll(".option");

selected.addEventListener("click", () => {
    optionsContainer.classList.toggle("active");
});

optionsList.forEach( x => {
    x.addEventListener("click", () => {
        if (x.querySelector("label").innerHTML != "Job Specialization"){
            document.getElementById("job_special").value = x.querySelector("label").innerHTML;
        }else{
            document.getElementById("job_special").value = ""
        }
        document.getElementById("selected-text").textContent = x.querySelector("label").innerHTML;
        optionsContainer.classList.remove("active");
    });
});

/*DATE POSTED DROP DOWN MENU FUNCTION*/
const selected_time = document.querySelector(".selected-time");
const time_optionsContainer = document.querySelector(".time-options-con");
const time_optionsList = document.querySelectorAll(".time-option");

selected_time.addEventListener("click", () => {
    time_optionsContainer.classList.toggle("active");
});

time_optionsList.forEach( y => {
    y.addEventListener("click", () => {
        document.getElementById("date_posted").value = y.querySelector("a").innerHTML;
        document.getElementById("time-text").textContent = y.querySelector("label").innerHTML;
        time_optionsContainer.classList.remove("active");
    });
});


/*BANNER AUTO SCROLL*/
onload  = start;
function start()
{
    var i = 1;
    function Move()
    {
        i = (i%2)+1;
        document.getElementById('i'+i).checked = true;
    }
    setInterval(Move,5000); //5 sec interval
}

/*PAGINATION*/
const ulTag = document.querySelector("#pagination");

function element(totalPages, page){
    let liTag = '';
    let activeLi;
    let beforePages = page - 1;
    let afterPages = page + 1;
    if (page > 1)//if page value is greater than 1 then add prev button
    {
        liTag += `<li class="btn prev" onclick="element(totalPages, ${page - 1})"><span><i class="fas fa-chevron-left"></i> Prev</span></li>`;
    }

    //how many pages or li show before the current li
    if (page == totalPages) //if page value is equal to totalPages then subtract by -2 to the beforePages value
    {
        beforePages = beforePages - 2;
    }
    else if (page == totalPages - 1) //if page value is equal to totalPages by -1 then subtract by -1 to the beforePages value
    {
        beforePages = beforePages - 1;
    }

    //how many pages or li show after the current li
    if (page == 1) //if page value is equal to 1 then add by +2 to the afterPages value
    {
        afterPages = afterPages + 2;
    }
    else if (page == 2) //if page value is equal to 2 then add by +1 to the afterPages value
    {
        afterPages = afterPages + 1;
    }

    for (let pageLength = beforePages; pageLength <= afterPages; pageLength++)
    {
        if (pageLength > totalPages)
        {
            continue;
        }
        else if (pageLength == 0) //if pageLength is equal to 0 then add 1 to the pageLength value
        {
            pageLength = pageLength + 1;
        }
        else if (page == pageLength) //if page value is equal to pagelength then assign active to activeLi
        {
            activeLi = "active";
        }
        else
        {
            activeLi = "";
        }
        liTag += `<li class="numb ${activeLi}" onclick="element(totalPages, ${pageLength})"><span>${pageLength}</span></li>`;
    }

    if (page < totalPages)//if page value is less than totalPages value then add next button
    {
        liTag += `<li class="btn next" onclick="element(totalPages, ${page + 1})"><span>Next <i class="fas fa-chevron-right"></i></span></li>`;
    }
    ulTag.innerHTML = liTag;
}



/*BACK TO TOP ANIMATION*/
const button = document.querySelector("#btnToTop");
btnToTop.addEventListener("click", function(){
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    });
});


