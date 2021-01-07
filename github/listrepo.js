const w3c_report = 'https://w3c.github.io/validate-repos/report.json';

var w3c_data;
var w3c_group;

function LoadData() {
  fetch(w3c_report, { mode: 'cors'})
  .then(function(response) {
    if (response.ok) {return response.json(); }
    throw Error("Returned response for data: " + response.status);
  }).then(function(data) {
    w3c_data = data.repos;
    w3c_group = data.groups;
  });
  document.getElementById('group_submit').addEventListener('click', ListRepositories);
}
window.addEventListener('load', LoadData);

function ListRepositories() {
  var gid = document.getElementById('group_id').value;
  var out = '';

  var ginfo = '';
  if (w3c_group[gid]) {
    ginfo = w3c_group[gid]['name'] + ' / ' + w3c_group[gid]['type'];
  }
  document.getElementById('group_info').innerText = ginfo;

  var cstr;
  w3c_data.forEach(elem => {
    if (elem.w3c && (elem.w3c.group == gid)) {
      out += '<tr>';
      cstr = elem.owner.login + '/' + elem.name;
      out += '<td><a href="https://github.com/' + cstr + '">' + cstr + '</td>';
      out += '<td>' + elem.createdAt + '</td>';
      out += '<td>' + elem.homepageUrl + '</td>';
      out += '<td>' + elem.isPrivate + '</td>';
      out += '<td>' + elem.defaultBranch.name + '</td>';
      out += '<td>' + elem.w3c['repo-type'][0] + '</td>';
      out += '</tr>';
    }
  });

  document.getElementById('repos_list').innerHTML = out;
}

