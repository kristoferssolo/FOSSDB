window.addEventListener("DOMContentLoaded", () => {
    const FORM_VERIFY = document.getElementsByClassName("verify")
    const SUBMIT_BUTTON = document.getElementById("submit-button")

    Array.from(FORM_VERIFY).forEach((input) => {
        input.addEventListener("input", () => {
            const ALL_FILLED = Array.from(FORM_VERIFY).every(
                (input) => input.value.trim() !== ""
            )
            if (ALL_FILLED) {
                SUBMIT_BUTTON.classList.remove(
                    "bg-slategray-200",
                    "text-lightsteelblue-100",
                    "opacity-50",
                    "cursor-default"
                )
                SUBMIT_BUTTON.classList.add(
                    "bg-skyblue-300",
                    "text-gray-500",
                    "opacity-100",
                    "hover:opacity-60"
                )
                SUBMIT_BUTTON.disabled = false
            } else {
                SUBMIT_BUTTON.classList.remove(
                    "bg-skyblue-300",
                    "text-gray-500",
                    "opacity-100",
                    "hover:opacity-60"
                )
                SUBMIT_BUTTON.classList.add(
                    "bg-slategray-200",
                    "text-lightsteelblue-100",
                    "opacity-50",
                    "cursor-default"
                )
                SUBMIT_BUTTON.disabled = true
            }
        })
    })
})
