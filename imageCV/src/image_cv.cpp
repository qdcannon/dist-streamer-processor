#include <iostream>
#include "../lib/cpp-httplib/httplib.h"
#include "../include/image_cv.hpp"

cv::Mat decode_data(std::vector<uchar> data) {
    // turn raw vector data into an image
    std::cout<< "Going to start parsing data... " << std::endl;
    //cv::Mat image = cv::imread(image_name); // Replace with your image path
    cv::Mat image = cv::imdecode(data, cv::IMREAD_COLOR);
    return image;
    
}

//why did I make it string instread of uchar vector?
std::string encode_data(cv::Mat mat){
 // Encode result back to JPEG
    std::vector<uchar> buf;
    cv::imencode(".jpg", mat, buf);
    std::string out(buf.begin(), buf.end());
    return out;
    
}

cv::Mat process_image(cv::Mat image){
    cv::Mat output;
    if (image.empty()) {
        std::cerr << "Could not open or find the image!\n";
        return output;
    }

    // Convert to grayscale
    cv::cvtColor(image, output, cv::COLOR_BGR2GRAY);

    // Apply Gaussian blur
    //cv::Mat blurred;
    //cv::GaussianBlur(gray, blurred, cv::Size(5, 5), 1.5);

    // Edge detection using Canny
    //cv::Mat edges;
    //cv::Canny(blurred, edges, 50, 150);

    // Show the images
    //cv::imshow("Original", image);
    //cv::imshow("Grayscale", gray);
    //cv::imshow("Edges", edges);

    // Save the edge image
    //cv::imwrite("edges_output.jpg", edges);
    //cv::imwrite("gray_output.jpg", gray);
    //cv::imwrite("image_output.jpg", image);

    // Wait for a key press indefinitely
   // cv::waitKey(0);
    return output;
    //return0;
}

bool start_server()
{
    httplib::Server svr;
    svr.Post("/process", [](const httplib::Request &req, httplib::Response &res) {
        std::vector<uchar> data(req.body.begin(), req.body.end());
        cv::Mat incoming_image = decode_data(data);
        cv::Mat outgoing_image = process_image(incoming_image);
        std::string outgoing_string = encode_data(outgoing_image);
        res.set_content(outgoing_string, "image/jpeg");
    });

    svr.listen("0.0.0.0", 8081);
    return true;
}

int main()
{

    if(start_server()!=0){
        return -1;
    }
    return 0;
}