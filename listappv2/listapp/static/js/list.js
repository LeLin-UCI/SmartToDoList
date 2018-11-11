var app = new Vue({
  el: '#app',
  data: {
    message: ''
  }
})

window.onload = function() {
	document.getElementById('submit').onclick = function() {
	  var list = document.getElementById('list');
	  var newLI = document.createElement('li');
	  newLI.innerHTML = 'A new item';
	  list.appendChild(newLI);
	  setTimeout(function() {
	    newLI.className = newLI.className + "show list-group-item list-group-item-action flex-column align-items-start";
	  }, 13);
	}
}

// <li class="list-group-item list-group-item-action">Dapibus ac facilisis in</li>
