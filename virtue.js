function checkOTP() {
    var enteredOTP = document.getElementById('otp').value;
    if (enteredOTP === '1122') {
        alert('OTP is successful!');
    } else {
        alert('Invalid OTP. Please try again.');
    }
}
