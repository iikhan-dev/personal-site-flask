const textContainer = document.getElementById("translated-text");
const languages = ["English", "French", "Spanish", "Arabic", "Urdu"];
let currentLanguageIndex = 0;

function translateText() {
    const translations = {
        English: "👋 Hello! I'm Ismail. 😃",
        French: "👋 Bonjour! Je suis Ismail. 😃",
        Spanish: "👋 ¡Hola! Soy Ismail. 😃",
        Arabic: "😃 .مرحبًا! أنا إسماعيل 👋",
        Urdu: "😃 .ہیلو! میں اسماعیل ہوں 👋",
    };

    currentLanguageIndex = (currentLanguageIndex + 1) % languages.length;
    const currentLanguage = languages[currentLanguageIndex];
    textContainer.textContent = translations[currentLanguage];
}

// Set an interval to periodically change the text
setInterval(translateText, 4500); // Change every 4.5 seconds
