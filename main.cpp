# include <iostream>
# include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main(int argc, char** argv)
{
    Mat src = imread("/home/xm/repository/opencv-study/lena.jpg");
    if (src.empty())
    {
        printf("could not load image ...\n");
            return -1;
    }

    namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);
    imshow("test opencv setup", src);
    waitKey(0);
    return 0;
}
