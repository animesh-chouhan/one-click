async function updateCount() {
    try {
        let res = await fetch("/count");
        let data = await res.json();
        document.getElementById("count").innerText = data.count;
    } catch (e) {
        console.error("Error fetching count:", e);
    }
}

async function clickOnce() {
    try {
        await fetch("/click", { method: "POST" });
        updateCount();
    } catch (e) {
        console.error("Error clicking:", e);
    }
}

document.getElementById("click-btn").addEventListener("click", clickOnce);

// Initial load
updateCount();

// Auto refresh every 2 seconds
setInterval(updateCount, 3000);