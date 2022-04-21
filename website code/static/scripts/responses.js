function getBotResponse(input) {
    //Wrong Product
    if (input == "wrong product") {
        return "let me verify";
    } else if (input == "i have recieved the wrong painting") {
        return "we will get back to you shortly";
    } else if (input == "i have recieved the wrong product") {
        return "we will verify and exchange the product";
    }

    // // Simple responses
    // if (input == "hello") {
    //     return "Hello there!";
    // } else if (input == "goodbye") {
    //     return "Talk to you later!";
    // } else {
    //     return "Try asking something else!";
    // }
}