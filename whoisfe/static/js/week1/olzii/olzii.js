window.jsPDF = window.jspdf.jsPDF;
var docPDF = new jsPDF();
function print() {
    var elementHTML = document.querySelector("#vn");
    docPDF.html(elementHTML, {
        callback: function (docPDF) {
            docPDF.save('CV_version_02.pdf');
        },
        x: 15,
        y: 15,
        width: 170,
        windowWidth: 650
    });
}