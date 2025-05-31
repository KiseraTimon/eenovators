// Run this function immediately when the page loads
document.addEventListener("DOMContentLoaded", () => {
    updateTariffValues();
});

function updateTariffValues() {
    let kplcVal = null;
    let spvVal = null;

    const rows = document.querySelectorAll(".deltas table tbody tr");

    rows.forEach(row => {
        const registerName = row.cells[0].innerText.trim();
        const value = parseFloat(row.cells[1].innerText);

        if (registerName === "KPLC Mains Combined*") {
            kplcVal = value;
        }
        if (registerName === "SPV") {
            spvVal = value;
        }
    });

    if (kplcVal !== null && spvVal !== null) {
        const consumption = kplcVal * spvVal;

        // Populate spans with values rounded to 3 decimals
        document.getElementById("consumption").innerText = consumption.toFixed(3);
        document.getElementById("generation").innerText = spvVal.toFixed(3);
    } else {
        document.getElementById("consumption").innerText = "N/A";
        document.getElementById("generation").innerText = "N/A";
    }
}

function tariffCalc() {
    const rate = parseFloat(document.getElementById('value').value);

    if (isNaN(rate) || rate < 0) {
        alert("Please enter a valid, non-negative tariff rate.");
        return;
    }

    const consumption = parseFloat(document.getElementById("consumption").innerText);

    if (isNaN(consumption)) {
        alert("Consumption value is missing or invalid.");
        return;
    }

    const charge = consumption * rate;

    const formatted = new Intl.NumberFormat('en-KE', {
        style: 'currency',
        currency: 'KES',
        minimumFractionDigits: 2
    }).format(charge);

    document.querySelector(".tariff-result h2").innerText = formatted;
}