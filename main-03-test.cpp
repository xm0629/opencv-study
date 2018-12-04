# include <iostream>
# include <opencv2/opencv.hpp>
# include <cmath>

using namespace std;
//图像的掩模操作提高图像的对比度

using namespace cv;
int main(int argc, char** argv)
{
    Mat src, dst;

    src = imread("/home/xm/repository/opencv-study/lena.jpg");
    if (!src.data)
    {
        printf("could not load image..\n");
        return -1;
    }
    namedWindow("input image", CV_WINDOW_AUTOSIZE);
    imshow("input image", src);
    
    int cols = (src.cols-1) * src.channels();
    int offsetx = src.channels;
    int row = src.row;


    for (int row=1;row < row-1; row++)
    {
        for (int col=offsetx; col<cols; col++)

    }


    waitKey(0);
    return 0;
}


