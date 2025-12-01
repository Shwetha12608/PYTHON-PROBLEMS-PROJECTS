import re
from nltk.corpus import stopwords
from collections import Counter
import nltk
nltk.download('stopwords')

# TECHNICAL SKILLS DICTIONARY

TECH_SKILLS = {
    "c", "c programming", "embedded", "embedded systems", "python",
    "stm32", "arduino", "esp32", "avr", "8051", "pic",
    "rtos", "freertos", "real-time", "os",
    "spi", "i2c", "uart", "can", "i2s",
    "microcontroller", "microcontrollers",
    "sensors", "pwm", "adc", "dac",
    "debugging", "troubleshooting", "fault", "fault finding",
    "interrupts", "timers", "communication", "protocols"
}


# Clean text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    words = text.split()

    stop_words = set(stopwords.words("english"))
    filtered = [w for w in words if w not in stop_words]

    return filtered

# ------------------------------------------
# Extract ONLY real technical skills
# ------------------------------------------
def extract_skills(words):
    found = set()

    for w in words:
        if w in TECH_SKILLS:
            found.add(w)

    return found

# ------------------------------------------
# ATS Match Score
# ------------------------------------------
def match_score(resume, jd):
    resume_words = clean_text(resume)
    jd_words = clean_text(jd)

    resume_skills = extract_skills(resume_words)
    jd_skills = extract_skills(jd_words)

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills

    score = (len(matched) / len(jd_skills)) * 100 if jd_skills else 0

    return round(score, 2), matched, missing

# ------------------------------------------
# DEMO
# ------------------------------------------
resume = """C programming, embedded systems, STM32, UART, SPI, I2C,
RTOS basics, problem solving, python projects, sensors, real-time systems"""

jd = """Looking for an embedded software engineer with strong C programming,
RTOS experience, microcontrollers like STM32, SPI/I2C interface,
debugging skills, UART, and basic python knowledge."""

score, matched, missing = match_score(resume, jd)

print("ATS Skill Match Score:", score, "%")
print("Matched Skills:", matched)
print("Missing Technical Skills:", missing)


