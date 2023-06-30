/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        "../templates/**/*.html",

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        "../../templates/**/*.html",

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        "../../**/templates/**/*.html",

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        colors: {
            darkslateblue: "#3d59a1",
            cornflowerblue: "#7aa2f7",
            gray: {
                100: "#37222c",
                200: "#1f2231",
                300: "#1a1b26",
                400: "#16161e",
                500: "#15161e",
            },
            darkslategray: {
                100: "#2c5a66",
                200: "#414868",
                300: "#3b4261",
                400: "#283457",
                500: "#292e42",
                600: "#20303b",
            },
            skyblue: {
                100: "#89ddff",
                200: "#2ac3de",
                300: "#0db9d7",
            },
            paleturquoise: "#b4f9f8",
            steelblue: {
                100: "#6183bb",
                200: "#536c9e",
                300: "#565f89",
                400: "#394b70",
            },
            cadetblue: {
                100: "#41a6b5",
                200: "#449dab",
                300: "#27a1b9",
            },
            lightskyblue: "#7dcfff",
            lightsteelblue: {
                100: "#c0caf5",
                200: "#a9b1d6",
            },
            indianred: {
                100: "#db4b4b",
                200: "#b2555b",
                300: "#914c54",
            },
            sienna: "#713137",
            slategray: {
                100: "#737aa2",
                200: "#545c7e",
            },
            mediumturquoise: "#73daca",
            lightgreen: "#9ece6a",
            teal: "#266d6a",
            burlywood: "#e0af68",
            mediumaquamarine: "#1abc9c",
            lightcoral: "#f7768e",
            mediumpurple: {
                100: "#bb9af7",
                200: "#9d7cd8",
            },
            sandybrown: "#ff9e64",
            deeppink: "#ff007c",
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
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
        require("@tailwindcss/line-clamp"),
        require("@tailwindcss/aspect-ratio"),
    ],
}
