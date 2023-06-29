Array.from(document.getElementsByClassName("remove-btn")).forEach((button) => {
    button.addEventListener("click", () => {
        console.log("TRUE")
        const hiddenDeleteInput = button.previousElementSibling
        hiddenDeleteInput.value = "on"
        button.parentElement.style.display = "none"
    })
})
window.addEventListener("DOMContentLoaded", () => {
    const FORM_VERIFY = document.getElementsByClassName("verify")
    const SUBMIT_BUTTON = document.getElementById("submit-button")
    SUBMIT_BUTTON.disabled = true

    Array.from(FORM_VERIFY).forEach((input) => {
        input.addEventListener("input", () => {
            const ALL_FILLED = Array.from(FORM_VERIFY).every(
                (input) => input.value.trim() !== ""
            )
            if (ALL_FILLED) {
                SUBMIT_BUTTON.classList.remove(
                    "submit-button-disabled",
                    "text-lightsteelblue-100",
                    "bg-slategray-200"
                )
                SUBMIT_BUTTON.classList.add(
                    "submit-button-enabled",
                    "text-gray-500",
                    "bg-skyblue-300"
                )
                SUBMIT_BUTTON.disabled = false
            } else {
                SUBMIT_BUTTON.classList.remove(
                    "submit-button-enabled",
                    "text-gray-500",
                    "bg-skyblue-300"
                )
                SUBMIT_BUTTON.classList.add(
                    "submit-button-disabled",
                    "text-lightsteelblue-100",
                    "bg-slategray-200"
                )
                SUBMIT_BUTTON.disabled = true
            }
        })
    })
})

window.addEventListener("DOMContentLoaded", () => {
    document
        .getElementById("menu-button")
        .addEventListener("click", function() {
            document.getElementById("dropdown-menu").style.display =
                this.ariaExpanded === "true" ? "none" : "flex"
            this.ariaExpanded = this.ariaExpanded === "true" ? "false" : "true"
        })
})
