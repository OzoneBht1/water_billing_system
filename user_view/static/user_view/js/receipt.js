$(document).ready(function () {
  window.jsPDF = window.jspdf.jsPDF;
  let btn = $("#resultsButton");
  btn.text("download");
  btn.on("click", () => {
    // $("#c-invoice").modal("show");
    setTimeout(function () {
      html2canvas(document.querySelector("#results"), {
        useCORS: true,
      }).then((canvas) => {
        //$("#previewBeforeDownload").html(canvas);
        var imgData = canvas.toDataURL("image/jpeg", 1);
        // imgData.width = 1000;
        // imgData.height = 1050;
        console.log(imgData);
        var pdf = new jsPDF("p", "mm", "a4");
        var pageWidth = pdf.internal.pageSize.getWidth();
        var pageHeight = pdf.internal.pageSize.getHeight();
        var imageWidth = canvas.width;
        var imageHeight = canvas.height;

        var ratio =
          imageWidth / imageHeight >= pageWidth / pageHeight
            ? pageWidth / imageWidth
            : pageHeight / imageHeight;
        //pdf = new jsPDF(this.state.orientation, undefined, format);
        console.log(ratio);
        console.log(imageWidth);
        console.log(imageHeight);
        pdf.addImage(
          imgData,
          "JPEG",
          0,
          0,
          //   imageWidth * 0.2,
          //   imageHeight * 0.2
          imageWidth * ratio,
          imageHeight * ratio
        );
        pdf.save("invoice.pdf");
        //$("#previewBeforeDownload").hide();
        // $("#c-invoice").modal("hide");
      });
    }, 500);
  });
});
