  tinyMCE.init({
    theme : "advanced",
    mode : "exact",
    language : "fr",
    elements : "id_description",
    plugins : "inlinepopups",
    theme_advanced_buttons1 : "formatselect,bold,italic,separator,bullist,numlist,separator,link,unlink,separator,undo,redo,separator,removeformat",
    theme_advanced_buttons2 : "",
    theme_advanced_buttons3 : "",
    theme_advanced_blockformats : "p,h3,h4,h5",
    theme_advanced_toolbar_location : "top",
    theme_advanced_resizing : true,
    theme_advanced_resize_horizontal : true,
    theme_advanced_statusbar_location : "bottom",
    debug : false,
    entity_encoding : "raw",
    valid_elements : "" +
"+a[rel|href|title]," +
"-strong/-b," +
"-em/-i," +
"#p[]," +
"-ol[]," +
"-ul[]," +
"-li[]," +
 "br,-h3,-h4,-h5,"
  });

function toggleEditor() {
  if (!tinyMCE.getInstanceById('id_description'))
  {
    tinyMCE.execCommand('mceAddControl', false, 'id_description');
    document.getElementById('togglegeditor_text').innerHTML = 'Désactiver ';
  }
  else
  {
    tinyMCE.execCommand('mceRemoveControl', false,'id_description');
    document.getElementById('togglegeditor_text').innerHTML = 'Activer  ';
  }
}
