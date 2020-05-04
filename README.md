# People Counter
## Primary Objective
Count the Number of Unique People with a Video

## About
See the Jupyter Notebooks for progress notes and samples.

## Overall Conclusion
Depending on the use case (e.g., face occlusions and reappearing faces or long classroom lessons), different processing strategies should be considered. Although face detection using Haar feature-based cascade classifiers (Viola-Jones) performs very well on the given videos (see the first notebook), face detection does not allow to store a facial id and to compare it against already classified ones. Thus, face recognition is mandatory for all use cases to reliable count the number of unique people.

There are, however, different paths one should consider:  
(1) For shorter videos with higher chances of face occlusion, a possible algorithm might be to initially convert the video into frames (2fps seems sufficient, see the second notebook) and then perform face recognition for every frame. The first frames should built-up a face store containing unique face ids. In consecutive frames, the detected faces should be compared against the face already classified within the store. For more accurate recognition/identification, a set of high-quality profile pictures can be provided beforehand to increase classification dramatically (see [Create and Train a Person Group](https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/client-libraries?tabs=windows&pivots=programming-language-python#create-and-train-a-person-group)).  
(2) For more extended video sessions (e.g., classroom lessons) with less frequent occlusions, converting the video and checking every frame might be too expensive regarding computational time/complexity. Therefore, it might be better to try to detect all face (and store them) within a video stream. After a face has been detected, the face should be tracked all time. After a face occlusion (or the subject simply leaves the frame, and re-enters), face detection should kick-in and check if that person is already a known face. If not, the face should be added to the face store. In any way, a person’s face should be tracked to avoid unnecessary face detection.

Moreover, if external APIs are used, it should be check which API (e.g., [Google Vison](https://cloud.google.com/vision), [Microsoft Face](https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/client-libraries?tabs=windows&pivots=programming-language-python), [Amazon Rekognition](https://aws.amazon.com/rekognition/)) peforms best (face recognition and possible emotion recognition) regarding human coders.



