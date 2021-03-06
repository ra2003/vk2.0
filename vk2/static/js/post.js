function show_actions_menu(){
    document.getElementById('actions_menu').setAttribute('class', 'ui_actions_menu_wrap _ui_menu_wrap shown')
}

function hide_actions_menu(){
    document.getElementById('actions_menu').setAttribute('class', 'ui_actions_menu_wrap _ui_menu_wrap')
}

function show_actions_menu_group(){
    document.getElementById('actions_menu1').setAttribute('class', 'ui_actions_menu_wrap _ui_menu_wrap shown')
}

function hide_actions_menu_group(){
    document.getElementById('actions_menu1').setAttribute('class', 'ui_actions_menu_wrap _ui_menu_wrap')
}

function delete_post(pk){
    event.preventDefault();
    $.ajax({
        type: 'GET',
        url: '/post/delete/?id='+pk,
        data: {'pk': pk},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function () {
            document.getElementById('post'+pk).remove();
        }
    });
}

function to_pin_post(pk) {
    event.preventDefault();
    let url = document.location.pathname;
    public_pk = url.split('/public')[1].split('/')[0];
    $.ajax({
        type: 'GET',
        url: '/post/pin/?id='+pk,
        data: {'pk': pk, 'public_pk': public_pk},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function () {
        }
    });
}
function like_post(pk){
    event.preventDefault();
    $.ajax({
        type: 'GET',
        url: '/post/put-like/?id='+pk,
        data: {'pk': pk},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            let data = JSON.parse(json.content);
            if (data.likes_put){
                document.getElementById('like_post'+pk).setAttribute('class', 'like_btn like _like animate active');
                document.getElementById('count_like_post'+pk).textContent = data.count_likes
            }else {
                document.getElementById('like_post'+pk).setAttribute('class', 'like_btn like _like animate');
                document.getElementById('count_like_post'+pk).textContent = data.count_likes
            }
        }
    });
}