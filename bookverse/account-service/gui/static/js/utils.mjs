export function showToast(text, type) {
    $('body').toast({
        class: type,
        message: text,
        displayTime: 10000,
        position: "bottom left",
        showProgress: "bottom",
        progressUp: false
    });
}
