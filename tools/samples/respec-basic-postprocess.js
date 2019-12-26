function addSelfLinks (config, document) {
    var lis = document.querySelectorAll("li[id]");
    lis.forEach(function(li) {
        var selfLink = document.createElement("a");
        selfLink.setAttribute("href", "#" + li.getAttribute("id"));
        selfLink.setAttribute("class", "self-link");
        li.prepend(selfLink);
    });
}
