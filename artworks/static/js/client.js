// var el = x => document.getElementById(x);

// function showPicker(inputId) { el('file-input').click(); }

// function showPicked(input) {
//     el('upload-label').innerHTML = input.files[0].name;
//     var reader = new FileReader();
//     reader.onload = function (e) {
//         el('image-picked').src = e.target.result;
//         el('image-picked').className = '';
//     }
//     reader.readAsDataURL(input.files[0]);
// }


// // function showImg(input){
// //     if (input.files && input.files[0]) {
// //         var reader = new FileReader();
        
// //         reader.onload = function (e) {
// //             $('#profile-img-tag').attr('src', e.target.result);
// //         }
// //         reader.readAsDataURL(input.files[0]);
// //     }
// // }
// // $("#file-input").change(function(){
// //     readURL(this);
// // });


// function analyze() {
//     var uploadFiles = el('file-input').files;
//     if (uploadFiles.length != 1) alert('Please select 1 file to analyze!');

//     el('analyze-button').innerHTML = 'Analyzing...';
//     var xhr = new XMLHttpRequest();
//     var loc = window.location
//     xhr.open('POST', `${loc.protocol}//${loc.hostname}:${loc.port}/analyze`, true);
//     xhr.onerror = function() {alert (xhr.responseText);}
//     xhr.onload = function(e) {
//         if (this.readyState === 4) {
//             var response = JSON.parse(e.target.responseText);
//             el('result-label').innerHTML = `${response['names'][0]} !`;
//             el('result-label1').innerHTML = `${response['names'][1]} !`;
//             el('result-label2').innerHTML = `${response['names'][2]} !`;
            
//             // console.log(document.getElementsByClassName("progress-bar")[0]);
//             // console.log(document.getElementsByClassName("progress-bar")[1]);
//             // console.log(document.getElementsByClassName("progress-bar")[2]);

//             $('#pb').attr('aria-valuenow', response['probs'][0]).css('width', response['probs'][0]*1000);
//             $('#pb1').attr('aria-valuenow', response['probs'][1]).css('width', response['probs'][1]*1000);
//             $('#pb2').attr('aria-valuenow', response['probs'][2]).css('width', response['probs'][2]*1000);

//             // el('probs-label').innerHTML = `${response['probs'][0]} !`;
//             // el('probs-label1').innerHTML = `${response['probs'][1]} !`;
//             // el('probs-label2').innerHTML = `${response['probs'][2]} !`;
//         }
//         el('analyze-button').innerHTML = 'Analyze';
//     }

//     var fileData = new FormData();
//     fileData.append('file', uploadFiles[0]);
//     xhr.send(fileData);
// }

// function removeHash () { 
//     var scrollV, scrollH, loc = window.location;
//     if ("pushState" in history)
//         history.pushState("", document.title, loc.pathname + loc.search);
//     else {
//         // Prevent scrolling by storing the page's current scroll offset
//         scrollV = document.body.scrollTop;
//         scrollH = document.body.scrollLeft;

//         loc.hash = "";

//         // Restore the scroll offset, should be flicker free
//         document.body.scrollTop = scrollV;
//         document.body.scrollLeft = scrollH;
//     }
// }

// function removeHash2() { 
//     history.replaceState(null, null, ' ');
//  }