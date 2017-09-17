function getValues() {
    return {
        'minutes': document.getElementById('slider-minute').noUiSlider.get(),
        'data': document.getElementById('slider-data').noUiSlider.get(),
        'sms': document.getElementById('slider-sms').noUiSlider.get()
    }
}

function calculate() {
    $.post({
        url: '/calculate/',
        data: getValues(),
        dataType: 'json',
        success: function(dataset) {
            var bestplan = null;
            var table = [];
            clearData(ChartValues);

            // Sort plans by Total Value
            sorted_plans = Object.keys(dataset).sort(function(a, b) {
                a_total = dataset[a].slice(-1).pop();
                b_total = dataset[b].slice(-1).pop();
                return parseFloat(a_total) - parseFloat(b_total)
            });

            // Alfaphebetic ordering
            sorted_plans.slice(0, 5).sort().forEach(function(label) {
                data = dataset[label];
                total = parseFloat(data.slice(-1).pop());

                if (bestplan == null || total < bestplan.value) {
                    bestplan = {plan: label, value: total};
                }

                addData(ChartValues, label, data.slice(3, 7));
            });

            updateTable(bestplan.plan, dataset[bestplan.plan]);
        }
    });
}


function normalizeInternet(value) {
    if (value >= 1000) {
        return value.toFixed() / 1000 + ' GB';
    }

    return value.toFixed() + ' MB';
}


function normalizeMinutes(value) {
    return `${value} min`;
}


function normalizeSms(value) {
    if (value == 1000) {
        return 'ilimitado';
    }
    return `${value} un`;
}


function normalizePrice(value) {
    return parseFloat(value).toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'});
}


function normalizeData(label, dataset) {
    [minutes, internet, sms, value, internet_package, sms_package, total] = dataset;

    minutes = normalizeMinutes(minutes);
    internet = normalizeInternet(internet);
    sms = normalizeSms(sms);
    value = normalizePrice(value);

    internet_package = normalizePrice(internet_package);
    sms_package = normalizePrice(sms_package);
    total = normalizePrice(total);

    return [
        label, minutes, internet, sms, value, internet_package, sms_package, total
    ];
}


function updateTable(label, data) {
    data = normalizeData(label, data);
    Table.clear();
    Table.rows.add([data]);
    Table.draw();
}


function addData(chart, label, data) {
    var color = "#"+((1<<24)*Math.random()|0).toString(16);

    chart.data.datasets.push({
        label: label,
        data: data,
        fill: false,
        backgroundColor: color,
        borderColor: color
    });
    chart.update();
}


function clearData(chart) {
    chart.data.datasets = [];
}


var Table = $('#bestplan').DataTable({
    ordering: false,
    searching: false,
    paging: false,
    info: false,
    columns: [
        {title: 'Plano', className: 'text-center'},
        {title: 'Minutos', className: 'text-center'},
        {title: 'Internet', className: 'text-center'},
        {title: 'SMS', className: 'text-center'},
        {title: 'Valor do Plano', className: 'text-center'},
        {title: 'Valor Pacote(s) Internet', className: 'text-center'},
        {title: 'Valor Pacote(s) SMS', className: 'text-center'},
        {title: 'Total', className: 'text-center'}
    ]
});


var ChartValues = new Chart($('#chart-values'), {
    type: 'line',
    data: {
        labels: ['VALOR DO PLANO', 'VALOR PACOTE INTERNET', 'VALOR PACOTE SMS', 'TOTAL (PLANO+PACOTES)'],
        datasets: []
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'COMPARATIVO ENTRE OS 5 MELHORES PLANOS'
        },
        tooltips: {
            position: 'average',
            mode: 'index',
            intersect: false,
            callbacks: {
                label: function(tooltipItem, chart) {
                    dataset = chart.datasets[tooltipItem.datasetIndex];
                    value = dataset.data[tooltipItem.index];

                    return `${dataset.label}: ${normalizePrice(value)}`;
                }
            }
        },
        scales: {
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'VALOR EM R$'
                }
            }]
        }
    }
});



$(function() {
    slider_minute = $("#slider-minute")
    slider_data = $("#slider-data")
    slider_sms = $("#slider-sms")

    noUiSlider.create(slider_minute.get(0), {
        start: [0],
        step: 100,
        range: {
            'min': [0],
            'max': [1000]
        },
        tooltips: {
            to: function(value) {
                return normalizeMinutes(value);
            }
        },
        pips: {
            mode: 'range',
            density: 3,
            format: {
                to: function(value) {
                    return normalizeMinutes(value);
                }
            }
        }
    });
    noUiSlider.create(slider_data.get(0), {
        start: [100],
        step: 100,
        range: {
            'min': [100],
            'max': [10000]
        },
        tooltips: {
            to: function(value) {
                return normalizeInternet(value);
            }
        },
        pips: {
            mode: 'range',
            density: 3,
            format: {
                to: function(value) {
                    return normalizeInternet(value);
                }
            }
        }
    });
    noUiSlider.create(slider_sms.get(0), {
        start: [0],
        step: 50,
        range: {
            'min': [0],
            'max': [1000]
        },
        tooltips: {
            to: function(value) {
                return normalizeSms(value);
            }
        },
        pips: {
            mode: 'range',
            density: 3,
            format: {
                to: function(value) {
                    return normalizeSms(value);
                }
            }
        }
    });

    slider_minute.get(0).noUiSlider.on('change', function() {
        calculate();
    });

    slider_data.get(0).noUiSlider.on('change', function() {
        calculate();
    });

    slider_sms.get(0).noUiSlider.on('change', function() {
        calculate();
    });

});
