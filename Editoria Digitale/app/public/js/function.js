let textBox = document.getElementById('textbox');

var ajax = null 
textBox.onkeyup = function() {

    var val = this.value;
    val = val.replace(/^\s|\s $/, "");
  
      if (val !== "") {
        searchForData(val);
      } else {
        try{
          document.getElementById('img_slot').style.display = 'none';
        }
        catch(e){}
        clearResult();
      }
  }

function searchForData(val) {
    if (ajax && typeof ajax.abort === "function") {
        try {
          document.getElementById("img_slot").style.display = "none"
        } catch (e) {}
        ajax.abort()
      }
      ajax = new XMLHttpRequest()
      ajax.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
          try {
            var obj = document.getElementById("found_products");
    
            var json = JSON.parse(this.responseText);
            console.log(json);
            for (var i = 0; i < 5; i++) {
              try {
                var x = document.getElementById("founded");
                x.remove();
              } catch (e) {}
            }
            for (var i = 0; i < 5; i++) {
                try {
                  document.getElementById("img_slot").style.display = "none";
                } catch (e) {}
      
                var div = document.createElement("div");
                div.setAttribute("id", "founded");
                div.setAttribute("onclick", "getClickedInfo()");
      
                div.setAttribute("pid", json.hits[i].objectID);
                div.setAttribute("product-name", json.hits[i].name);
                div.setAttribute("product-image", json.hits[i].thumbnail_url);
                div.setAttribute(
                  "product-url",
                  "https://stockx.com/" + json.hits[i].url
                );
                div.setAttribute("product-sku", json.hits[i].style_id);
                div.setAttribute("brand", json.hits[i].brand);
                div.setAttribute("retail", json.hits[i].price);
      
                obj.appendChild(div);
                var span = document.createElement("span");
      
                span.setAttribute("id", "clickable");
      
                span.setAttribute("pid", json.hits[i].objectID);
                span.setAttribute("product-name", json.hits[i].name);
                span.setAttribute("product-image", json.hits[i].thumbnail_url);
                span.setAttribute(
                  "product-url",
                  "https://stockx.com/" + json.hits[i].url
                );
                span.setAttribute("product-sku", json.hits[i].style_id);
                span.setAttribute("brand", json.hits[i].brand);
                span.setAttribute("retail", json.hits[i].price);
      
                span.textContent = json.hits[i].name;
                var img = document.createElement("IMG");
                img.setAttribute("src", json.hits[i].thumbnail_url);
      
                img.setAttribute("pid", json.hits[i].objectID);
                img.setAttribute("product-name", json.hits[i].name);
                img.setAttribute("product-image", json.hits[i].thumbnail_url);
                img.setAttribute(
                  "product-url",
                  "https://stockx.com/" + json.hits[i].url
                );
                img.setAttribute("product-sku", json.hits[i].style_id);
                img.setAttribute("id", "clickable");
                img.setAttribute("brand", json.hits[i].brand);
                img.setAttribute("retail", json.hits[i].price);
      
                div.appendChild(img);
                div.appendChild(span);
              }
        } catch (e) {}
    }
    }
    ajax.open(
        "POST",
        "https://xw7sbct9v6-dsn.algolia.net/1/indexes/products/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.4)%3B%20Browser",
        true
      );
      ajax.setRequestHeader("x-algolia-application-id", "XW7SBCT9V6");
      ajax.setRequestHeader(
        "x-algolia-api-key",
        "6b5e76b49705eb9f51a06d3c82f7acee"
      );
      ajax.send(`{"query":"` + val + `","facets":"*","filters":""}`);
    
}

function clearResult() {
    for (var i = 0; i < 5; i++) {
      try {
        var x = document.getElementById("founded");
        x.remove();
      } catch (e) {}
    }
}

function getClickedInfo() {
    document.onclick = function (e) {
      if (e.target.id == "founded" || e.target.id == "clickable") {
        var pid = e.target.getAttribute("pid");
        var product_name = e.target.getAttribute("product-name");
        var product_image = e.target.getAttribute("product-image");
        try {
          var product_sku = e.target.getAttribute("product-sku");
        } catch {
          var product_sku = "-";
        }
  
        for (var i = 0; i < 5; i++) {
          try {
            var x = document.getElementById("founded");
            x.remove();
          } catch (e) {}
        }
        document.getElementById("product_pid").value = pid;
        document.getElementById("textbox").value = product_name;
        document.getElementById("product_name").value = product_name;
        document.getElementById("product_image").value = product_image;
        if (product_sku === "") {
          document.getElementById("product_sku").value = "-";
        } else {
          document.getElementById("product_sku").value = product_sku;
        }
  
        document.getElementById("img_slot").setAttribute("src", product_image);
      } else {
      }
    };
  }