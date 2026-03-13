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

document.addEventListener("DOMContentLoaded", () => {
    void loadProjects()
})
