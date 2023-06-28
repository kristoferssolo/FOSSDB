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
