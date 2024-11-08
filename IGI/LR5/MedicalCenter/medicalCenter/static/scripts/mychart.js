
let eps = 0.1; //[0, inf]
let h = 0.05 // шаг

function calc()
{
    xs = [];
    ys = [];
    for (let i = -1; i <= 1; i += h)
    {
        xs.push(i.toFixed(2));
        ys.push(my_exp(i, eps));
    }
    return [xs, ys];
}

function my_exp(x, eps) {
    let sum = 0; 
    let factorial = 1; 
    let list = [];
    
    for (let i = 0; i < 501; i++) {
        if (i > 0) {
            factorial *= i;
        }
        
        let term = (x ** i) / factorial;
        list.push(term);
        sum += term;

        if (Math.abs(term) <= eps) {
            break;
        }
    }

    return sum;
}

function autocalc()
{
    ys2 = [];
    for (let i = -1; i <= 1 ; i += h)
    {
        ys2.push(Math.exp(i));
    }
    return ys2;
}

const ctx = document.getElementById('myChart').getContext('2d');

const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: calc()[0],
        datasets: [
            {
                label: 'Разложение по Тейлору',
                data: calc()[1],
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
                pointRadius: 3,
                pointHoverRadius: 10,
                pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                pointHoverBackgroundColor: 'rgba(255, 99, 132, 1)',
                animation: {
                    duration: 2000,
                    easing: 'easeOutBounce'
                }
            },
            {
                label: 'Автоматический расчет',
                data: autocalc(),
                borderColor: 'rgba(153, 102, 255, 1)',
                fill: false,
                pointRadius: 3,
                pointHoverRadius: 10,
                pointBackgroundColor: 'rgba(153, 102, 255, 1)',
                pointHoverBackgroundColor: 'rgba(255, 99, 132, 1)',
                animation: {
                    duration: 2000,
                    easing: 'easeOutBounce'
                }
            }
        ]
    },
    options: {
        responsive: true,

        animation: {
            duration: 3000, // Длительность анимации в миллисекундах
            easing: 'easeInOutQuart' // Тип анимации
        },
        plugins: {
            legend: {
                position: 'top',
            },
            annotation: {
                annotations: {
                    // arrow: {
                    //     type: 'line',
                    //     xMin: 18,
                    //     xMax: 20,
                    //     yMin: -1,
                    //     yMax: 0,
                    //     borderColor: 'rgba(255, 99, 132, 1)',
                    //     borderWidth: 2,
                    // },
                    // arrowhead1: {
                    //     type: 'line',  
                    //     xMin: 20,
                    //     xMax: 20,
                    //     yMin: -0.25,
                    //     yMax: 0,
                    //     borderColor: 'rgba(255, 99, 132, 1)', 
                    //     borderWidth: 2,
                    // },
                    // arrowhead2: {
                    //     type: 'line',  
                    //     xMin: 19.2,
                    //     xMax: 20,
                    //     yMin: -0.15,
                    //     yMax: 0,
                    //     borderColor: 'rgba(255, 99, 132, 1)', 
                    //     borderWidth: 2,
                    // },
                    // label1: {
                    //     type: 'label',
                    //     xValue: 22,
                    //     yValue: 0.4,
                    //     backgroundColor: 'rgba(245,245,245)',
                    //     content: ['Точка, с которой начинается', 'разложение по Тейлору'],
                    //     font: {
                    //         size: 18
                    //     }
                    // },
                    label2: {
                        type: 'label',
                        xValue: 7,
                        yValue: -2.5,
                        backgroundColor: 'rgba(245,245,245)',
                        content: ['Демонстрация графиков, полученных', 'по Тейлору и с помощью модуля Math'],
                        font: {
                            size: 18
                        }
                    }
                }
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Значение X'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Значение Y'
                }
            }
        }
    }
});
