/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 6;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 100.0, "KoPercent": 0.0};
    var dataset = [
        {
            "label" : "KO",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "OK",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.9230769230769231, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getTime"], "isController": false}, {"data": [0.5, 500, 1500, "36.7.144.246\/fins-console-middle\/group\/getTreeList"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckStatistics"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckOverTimeList"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getTabNum"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckList"], "isController": false}, {"data": [0.0, 500, 1500, "36.7.144.246\/fins-console-sso\/user\/login"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-sso\/sysMaintainConfig\/getSysNoticeConfig"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/loanProgress\/getList"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-sso\/sysMenu\/getAll"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-sso\/user\/appList?channel=PC"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/home\/getRemindMatters"], "isController": false}, {"data": [0.5, 500, 1500, "36.7.144.246\/fins-console-sso\/sysDict\/getAllDictItems?productCode=PRODUCT_SBED"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-sso\/user\/getSysConfig"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheckAutoCallRecord\/findByPage"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/operateReceiver"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckOrderTimeList"], "isController": false}, {"data": [0.5, 500, 1500, "36.7.144.246\/fins-console-sso\/user\/remindMatterList?channel=PC"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/toReassign\/getList"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/snatchConfig"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheckAutoCallRecord\/transferLabor"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getPhoneCheckSnatchMsg"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/intoManage\/getLoanArchiveList"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckerList"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-sso\/user\/chkApp"], "isController": false}, {"data": [1.0, 500, 1500, "36.7.144.246\/fins-console-middle\/phoneCheck\/snatchConfigQuery"], "isController": false}, {"data": [0.9444444444444444, 500, 1500, "36.7.144.246\/fins-console-middle\/loanInvest\/getList"], "isController": false}, {"data": [0.5, 500, 1500, "36.7.144.246\/fins-console-middle\/intoManage\/getOrgTree"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 65, 0, 0.0, 221.20000000000002, 44, 2202, 599.1999999999999, 1046.9999999999984, 2202.0, 0.8215784417816876, 18.961181208605087, 0.7918801585646392], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getTime", 1, 0, 0.0, 56.0, 56, 56, 56.0, 56.0, 56.0, 17.857142857142858, 7.795061383928571, 14.317103794642858], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/group\/getTreeList", 1, 0, 0.0, 781.0, 781, 781, 781.0, 781.0, 781.0, 1.2804097311139564, 6.290763044174136, 1.1366137163892445], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckStatistics", 1, 0, 0.0, 72.0, 72, 72, 72.0, 72.0, 72.0, 13.888888888888888, 6.266276041666667, 11.881510416666668], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckOverTimeList", 1, 0, 0.0, 77.0, 77, 77, 77.0, 77.0, 77.0, 12.987012987012989, 5.2252435064935066, 15.384030032467532], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getTabNum", 1, 0, 0.0, 316.0, 316, 316, 316.0, 316.0, 316.0, 3.1645569620253164, 1.4061263844936709, 2.6793660996835444], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckList", 1, 0, 0.0, 117.0, 117, 117, 117.0, 117.0, 117.0, 8.547008547008549, 3.4388354700854697, 9.89082532051282], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/user\/login", 1, 0, 0.0, 2202.0, 2202, 2202, 2202.0, 2202.0, 2202.0, 0.45413260672116257, 3.339471219346049, 0.35346063237965486], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/sysMaintainConfig\/getSysNoticeConfig", 1, 0, 0.0, 44.0, 44, 44, 44.0, 44.0, 44.0, 22.727272727272727, 9.12198153409091, 20.374644886363637], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/loanProgress\/getList", 6, 0, 0.0, 126.33333333333333, 78, 195, 195.0, 195.0, 195.0, 1.037344398340249, 2.2992441433264177, 1.0793852113589213], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/sysMenu\/getAll", 1, 0, 0.0, 189.0, 189, 189, 189.0, 189.0, 189.0, 5.291005291005291, 126.1729083994709, 4.536623677248677], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/user\/appList?channel=PC", 1, 0, 0.0, 74.0, 74, 74, 74.0, 74.0, 74.0, 13.513513513513514, 93.90836148648648, 10.187922297297298], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/home\/getRemindMatters", 1, 0, 0.0, 60.0, 60, 60, 60.0, 60.0, 60.0, 16.666666666666668, 7.356770833333334, 13.753255208333334], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/sysDict\/getAllDictItems?productCode=PRODUCT_SBED", 1, 0, 0.0, 1161.0, 1161, 1161, 1161.0, 1161.0, 1161.0, 0.8613264427217916, 392.0330668604651, 0.6552473621877691], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/user\/getSysConfig", 1, 0, 0.0, 49.0, 49, 49, 49.0, 49.0, 49.0, 20.408163265306122, 8.82892219387755, 17.87707270408163], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheckAutoCallRecord\/findByPage", 11, 0, 0.0, 88.45454545454545, 59, 239, 209.6000000000001, 239.0, 239.0, 0.903194022497742, 1.4919860774694145, 0.9219571085474998], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/operateReceiver", 2, 0, 0.0, 88.0, 82, 94, 94.0, 94.0, 94.0, 0.8756567425569177, 0.3523150175131349, 0.7405456436077058], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckOrderTimeList", 1, 0, 0.0, 61.0, 61, 61, 61.0, 61.0, 61.0, 16.393442622950822, 6.595799180327869, 19.435194672131146], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/user\/remindMatterList?channel=PC", 1, 0, 0.0, 1477.0, 1477, 1477, 1477.0, 1477.0, 1477.0, 0.6770480704129993, 0.3656324052132701, 0.5044801540284359], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/toReassign\/getList", 1, 0, 0.0, 69.0, 69, 69, 69.0, 69.0, 69.0, 14.492753623188406, 7.218070652173912, 14.917346014492752], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/snatchConfig", 1, 0, 0.0, 116.0, 116, 116, 116.0, 116.0, 116.0, 8.620689655172413, 3.468480603448276, 11.087351831896552], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheckAutoCallRecord\/transferLabor", 1, 0, 0.0, 145.0, 145, 145, 145.0, 145.0, 145.0, 6.896551724137931, 2.976831896551724, 5.825700431034483], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getPhoneCheckSnatchMsg", 1, 0, 0.0, 53.0, 53, 53, 53.0, 53.0, 53.0, 18.867924528301884, 7.591391509433962, 16.214622641509436], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/intoManage\/getLoanArchiveList", 5, 0, 0.0, 91.8, 83, 107, 107.0, 107.0, 107.0, 1.101079057476327, 1.753769475335829, 1.1234447258313145], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/getCheckerList", 7, 0, 0.0, 96.42857142857143, 60, 209, 209.0, 209.0, 209.0, 0.7825600894354389, 0.9466487912241476, 0.7057015092230297], "isController": false}, {"data": ["36.7.144.246\/fins-console-sso\/user\/chkApp", 1, 0, 0.0, 64.0, 64, 64, 64.0, 64.0, 64.0, 15.625, 21.728515625, 12.542724609375], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/phoneCheck\/snatchConfigQuery", 1, 0, 0.0, 201.0, 201, 201, 201.0, 201.0, 201.0, 4.975124378109452, 6.097442475124378, 4.037430037313433], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/loanInvest\/getList", 9, 0, 0.0, 175.66666666666669, 98, 691, 691.0, 691.0, 691.0, 0.9348706762231225, 2.010235697777085, 1.0109506466188842], "isController": false}, {"data": ["36.7.144.246\/fins-console-middle\/intoManage\/getOrgTree", 4, 0, 0.0, 593.0, 578, 610, 610.0, 610.0, 610.0, 0.09586349038968509, 22.172176820208023, 0.07896567787470642], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Percentile 1
            case 8:
            // Percentile 2
            case 9:
            // Percentile 3
            case 10:
            // Throughput
            case 11:
            // Kbytes/s
            case 12:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": []}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 65, 0, null, null, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
