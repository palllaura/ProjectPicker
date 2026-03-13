async function loadProjects() {
    try {
        const response = await fetch("/projects")

        if (!response.ok) {
            throw new Error("Failed to fetch projects")
        }

        const projects = await response.json()

        const select = document.getElementById("projects")

        projects.forEach(project => {
            const option = document.createElement("option")
            option.value = project.id
            option.textContent = project.name
            select.appendChild(option)
        })

    } catch (error) {
        console.error("Error loading projects:", error)
    }
}

function setupForm() {
    const form = document.getElementById("assignment-form")

    form.addEventListener("submit", async (event) => {
        event.preventDefault()

        const formData = new FormData(form)

        const projects = Array.from(
            document.getElementById("projects").selectedOptions
        ).map(option => Number(option.value))

        const payload = {
            name: formData.get("name"),
            email: formData.get("email"),
            experience_level: formData.get("experience_level"),
            primary_stack: formData.get("primary_stack"),
            preferred_duration: formData.get("preferred_duration"),
            skills: formData.get("skills"),
            projects: projects,
            availability_confirmed: formData.get("availability_confirmed") === "on"
        }

        try {
            const response = await fetch("/users/submit", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })

            if (!response.ok) {
                const error = await response.json()
                console.error("Backend validation error:", error)
                throw new Error("Failed to save profile")
            }

            const result = await response.json()
            fillForm(result.user)

        } catch (error) {
            console.error("Error submitting form:", error)
        }
    })
}

function fillForm(user) {
    const form = document.getElementById("assignment-form")

    form.name.value = user.name
    form.email.value = user.email
    form.experience_level.value = user.experience_level
    form.primary_stack.value = user.primary_stack
    form.skills.value = user.skills || ""

    const duration = document.querySelector(
        `input[name="preferred_duration"][value="${user.preferred_duration}"]`
    )

    if (duration) {
        duration.checked = true
    }

    const select = document.getElementById("projects")

    Array.from(select.options).forEach(option => {
        option.selected = user.projects.includes(Number(option.value))
    })
}

document.addEventListener("DOMContentLoaded", () => {
    void loadProjects()
    setupForm()
})