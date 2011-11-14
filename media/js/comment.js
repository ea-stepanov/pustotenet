var is_started = false;

function empty_field(text) {
  if (!is_started && document.formcomment.id_message.value == text) {
    document.formcomment.id_message.value = "";
    is_start = true;
  }
}