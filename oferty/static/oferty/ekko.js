
$(function() {
    function reposition() {
        var modal = $(this),
            dialog = modal.find('.lightbox');
        modal.css('display', 'block');
        
        // Dividing by two centers the modal exactly, but dividing by three 
        // or four works better for larger screens.
        dialog.css("margin-top", Math.max(0, ($(window).height() - dialog.height()) / 2));
    }
    // Reposition when a modal is shown
    $('.lightbox').on('show.bs.modal', reposition);
    // Reposition when the window is resized
    $(window).on('resize', function() {
        $('.lightbox:visible').each(reposition);
    });
});

$(document).on('click', '[data-toggle="lightbox"]', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});
