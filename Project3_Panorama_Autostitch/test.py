import unittest
import numpy as np
import warp
import alignment
import blend
import cv2

class TestWarp(unittest.TestCase):
    '''These TestCases tests the warping functions.'''
    @classmethod
    def setUp(self):
        ''' Run the warps once (independent of thresholds) '''
        #blank image
        blank = np.asarray(np.ones((40, 40, 3))*255.0, dtype=np.uint8)
        #simple grid image
        grid = np.asarray(np.ones((40, 40, 3))*255.0, dtype=np.uint8)
        grid[(10,30),:,:]=0
        grid[:,(10,30),:]=0
        parameters = (20,0.1,-0.1)

        resBl = np.load('testMat/warpBlank.npy')

        # 빈칸
        # Spherical Warping을 위해 warpSpherical 함수에 올바른 입력을 전달하시오.
        self.img_bl = warp.warpSpherical(__________, __________, __________, __________)
        self.org_bl = resBl


    def test_computeSphericalWarpMappings(self):
        ''' Check if spherical warp is correct. '''
        self.assertTrue(np.allclose(self.img_bl, self.org_bl, rtol=1e-05, atol=1e-05),
            'Error in Spherical warping'
        )


class TestAlignment(unittest.TestCase):
    '''These TestCases tests the alignment functions.'''

    @classmethod
    def setUp(self):
        self.f1 = []
        self.f2 = []
        self.matches = []

        self.outlier_f1 = cv2.KeyPoint(2,2,4)
        self.outlier_f2 = cv2.KeyPoint(3,3,4)

        for i in range(4):
            feature = cv2.KeyPoint(i//2,i%2, 4)
            self.f1.append(feature)
            self.f2.append(feature)
            match = cv2.DMatch()
            match.queryIdx = i
            match.trainIdx = i
            match.distance = 0
            self.matches.append(match)

        self.matches_with_outlier = self.matches[:]
        match = cv2.DMatch()
        match.queryIdx = 4
        match.trainIdx = 4
        match.distance = 0
        self.matches_with_outlier.append(match)

    def tearDown(self):
        pass

    def test_computehomography2(self):
        '''Tests A matrix from TODO 2'''
        # Place holder to get A from computeHomography
        A_student = np.zeros((8, 9))

        # 빈칸
        # computeHomography 함수에 feature 집합과 match, A 행렬을 전달하시오.
        alignment.computeHomography(__________, __________, __________, __________)

        A_soln = np.load('testMat/identityA.npy')
        self.assertTrue(np.allclose(A_soln, A_student, rtol=1e-05, atol=1e-05),
            'Error in Filling in A Matrix'
        )
    def test_computehomography3(self):
        '''Tests A matrix from TODO 3'''

        # 빈칸
        # Homography 행렬 H를 반환하도록 computeHomography를 호출하시오.
        H_student = alignment.computeHomography(__________, __________, __________)

        H_student = H_student.astype(float)
        H_student = H_student/H_student[2,2]
        self.assertTrue(np.allclose(np.eye(3), H_student, rtol=1e-05, atol=1e-05),
            'Error in Computing Homography'
        )
    def test_alignPair(self):
        '''Tests TODO 4'''

        # 빈칸
        # alignPair 함수에 feature, match, motion model 등을 올바르게 전달하시오.
        M = alignment.alignPair(__________, __________, __________, __________, __________, __________)

    def test_getInliers(self):
        '''Tests TODO 5'''

        # 빈칸
        # RANSAC threshold=1 일 때 inlier를 구하시오.
        inliers = alignment.getInliers(__________, __________, __________, __________, __________)
        self.assertTrue(len(inliers)==4,"Error in getting inliers")

        # 빈칸
        # RANSAC threshold=2 일 때 inlier를 구하시오.
        inliers = alignment.getInliers(__________, __________, __________, __________, __________)
        self.assertTrue(len(inliers)==5,"Error in getting inliers")

    def test_leastSquaresFit(self):
        '''Tests TODO 6,7'''

        # 빈칸
        # 첫 번째 inlier 집합에 대해 leastSquaresFit을 수행하시오.
        M = alignment.leastSquaresFit(__________, __________, __________, __________, __________)
        M = M.astype(float)
        M = M/M[2,2]
        self.assertTrue(np.allclose(np.eye(3), M, rtol=1e-05, atol=1e-05),
            'Error in least square fitting'
        )

        # 빈칸
        # 두 번째 inlier 집합에 대해 leastSquaresFit을 수행하시오.
        M = alignment.leastSquaresFit(__________, __________, __________, __________, __________)
        M = M.astype(float)
        M = M/M[2,2]
        transform = np.array([[0.9,0,0],[0,0.9,0],[-0.1,-0.1,1]])
        self.assertTrue(np.allclose(transform, M, rtol=1e-05, atol=1e-05),
            'Error in least square fitting'
        )

class TestBlend(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.testimage = np.zeros((10,10,3))
        self.rot_trans_transform = np.array([[np.cos(np.pi/4),-np.sin(np.pi/4),5],[np.sin(np.pi/4),np.cos(np.pi/4),-5],[0,0,1]])
        self.rot_trans_transform1 = np.array([[1,0,-5],[0,1,5],[0,0,1]])
        self.rot_trans_transform2 = np.array([[1,0,5],[0,1,-5],[0,0,1]])

        self.acc = np.zeros((50,75,4))
        self.img1 = np.ones((50,50,3))
        self.img2 = np.full((50,50,3),2)
        self.transform = np.array([[1,0,25],[0,1,0],[0,0,1]])


    def test_imageBoundingBox(self):
        '''Tests TODO 8'''

        # 빈칸
        # imageBoundingBox 호출 시 이미지와 Homography 행렬을 전달하시오.
        minX,minY,maxX,maxY = blend.imageBoundingBox(__________, __________)

        sol_minX,sol_minY,sol_maxX,sol_maxY = \
            int(5-9*np.sin(np.pi/4)),int(-5),int(5+9*np.sin(np.pi/4)),int(18*np.sin(np.pi/4)-5)
        self.assertAlmostEqual(minX, sol_minX,
            msg='Expected bounding box min x to be {} +/-1 but got {}.'.format(sol_minX,
            minX),
            delta=1.01,
        )
        self.assertAlmostEqual(maxY, sol_maxY,
            msg='Expected bounding box max y to be {} +/-1 but got {}.'.format(sol_maxY,
            maxY),
            delta=1.01,
        )
        self.assertAlmostEqual(maxX, sol_maxX,
            msg='Expected bounding box max x to be {} +/-1 but got {}.'.format(sol_maxX,
            maxX),
            delta=1.01,
        )
        self.assertAlmostEqual(minY, sol_minY,
            msg='Expected bounding box min y to be {} +/-1 but got {}.'.format(sol_minY,
            minY),
            delta=1.01,
        )

    def test_getAccSize(self):
        '''Tests TODO 9'''
        ipv = [blend.ImageInfo("test1",self.testimage,self.rot_trans_transform1),
            blend.ImageInfo("test2",self.testimage,self.rot_trans_transform2)]

        # 빈칸
        # getAccSize 호출 시 이미지 정보 리스트를 전달하시오.
        accWidth, accHeight, channels, width, translation = blend.getAccSize(__________)

        self.assertAlmostEqual(accWidth, 20,
            msg='Expected acc width to be {} +/-1 but got {}.'.format(20,
            accWidth),
            delta=1.01,
        )
        self.assertAlmostEqual(accHeight, 20,
            msg='Expected acc height to be {} +/-1 but got {}.'.format(20,
            accHeight),
            delta=1.01,
        )


if __name__ == '__main__':
    unittest.main()
