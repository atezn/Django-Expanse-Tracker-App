const myChart = document.querySelector('.my-chart');
const ul = document.querySelector('.expense-stats .details ul');


function createChart(chartData) {
    new Chart(myChart, {
        type: 'doughnut',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Expenses',
                data: chartData.data,
                backgroundColor: [
                    '#FF6384',
                    '#36A2EB',
                    '#FFCE56',
                    '#4BC0C0',
                    '#9966FF',
                    '#FF9F40'
                ]
            }]
        },
        options: {
            borderWidth: 3,
            borderRadius: 7.5,
            hoverBorderWidth: 0,
            plugins: {
                legend: {
                    display: true,
                    position: 'right'
                }
            }
        }
    });
}


function populateUl(chartData) {
    ul.innerHTML = ''; 
    chartData.labels.forEach((label, index) => {
        let li = document.createElement('li');
        li.innerHTML = `${label}: <span class='percentage'>$${chartData.data[index].toFixed(2)}</span>`;
        ul.appendChild(li);
    });
}



async function initializeChart() {
    try {
        const response = await fetch('/chart-data/');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const chartData = await response.json();
        createChart(chartData);
        populateUl(chartData);
    } catch (error) {
        console.error('Error loading chart data:', error);
        document.querySelector('.chart-container').innerHTML = 
            '<p class="error">Error loading chart data. Please try again later.</p>';
    }
}


initializeChart();