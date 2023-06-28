/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js}"],
    theme: {
        colors: {
            gray: {
                100: "#1a1b26",
                200: "#15161e",
                300: "#16161e",
            },
            indianred: "#db4b4b",
            burlywood: "#e0af68",

            lightsteelblue: {
                100: "#c0caf5",
                200: "#a9b1d6",
            },
            skyblue: "#0db9d7",
            crimson: "#f52a65",
            slategray: "#737aa2",
        },
        fontFamily: {
            rationale: [
                "Rationale",
                "Roboto",
                "Helvetica",
                "Arial",
                "sans-serif",
            ],
            abel: ["Abel", "Roboto", "Helvetica", "Arial", "sans-serif"],
            condensed: [
                "Roboto Condensed",
                "Roboto",
                "Helvetica",
                "Arial",
                "sans-serif",
            ],
            roboto: ["Roboto", "Helvetica", "Arial", "sans-serif"],
        },
        fontSize: {
            base: "1rem",
            xl: "1.25rem",
            "4xl": "4rem",
        },
        extend: {},
    },
    plugins: [],
}
