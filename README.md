# Drone Crop Monitoring

![Demo img](https://raw.githubusercontent.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter/main/img_asset/Screenshot%202023-05-11%20at%201.03.39%20AM.png)

[![git flutter repo](https://img.shields.io/badge/Flutter-Application-blue?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter) [ ![git web rep](https://img.shields.io/badge/Web-API-blue?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/jashanpreet-singh-99/Drone_crop_monitoring_web_api) [![git CNN repo](https://img.shields.io/badge/CNN-Model-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jashanpreet-singh-99/Drone_Crop_monitoring)   

Please take author's permission before usign the code.

## Overview

The project comprises three integral components, each serving a distinct purpose in the overall system. The first component entails a sophisticated client-side application designed to efficiently control and monitor the agricultural crops from the clients' perspective. This application offers comprehensive functionality, allowing users to oversee crop conditions, make informed decisions, and optimize farm management processes. 

Acting as a crucial intermediary, the second component is a robust Flask API that facilitates seamless communication and data exchange between the 3D simulator and the client application. This API serves as a reliable interface, enabling real-time interaction and data transmission, thereby enhancing the user experience and ensuring smooth integration between the various components of the system.

The third component, a cutting-edge 3D simulator, emulates a real-world farm environment and incorporates a drone equipped with advanced imaging capabilities. This simulated drone autonomously traverses the entire farm, capturing high-resolution images of the crops. These images are subsequently fed into a convolutional neural network (CNN) model, specifically developed for this project. The CNN model, constructed using a custom architecture, plays a pivotal role in detecting and classifying diseases within the crops. It leverages state-of-the-art transfer learning models as benchmarks to ascertain its performance and efficacy.

The intricate synergy among these components empowers the system to revolutionize agricultural practices. Through seamless integration, intelligent data analysis, and advanced imaging technology, the project strives to enhance crop monitoring, enable timely disease detection, and facilitate informed decision-making processes for optimized farm management.

## Client-side Application

The client-side application is meticulously developed using the Flutter framework, ensuring its cross-platform compatibility across multiple devices. Leveraging the versatility of Flutter, the application seamlessly caters to a wide range of operating systems and devices, allowing users to access its features regardless of their preferred platform.

One of the remarkable strengths of the client-side application lies in its optimal utilization of the expansive screen real estate offered by desktop devices. By capitalizing on the available space, the application delivers a rich and immersive user experience, presenting users with comprehensive control and monitoring capabilities for their agricultural crops. 

The application boasts two main pages, meticulously designed to cater to the diverse needs of users. Each page is thoughtfully crafted with a user-centric approach, prioritizing usability and intuitive navigation. These pages serve as the primary interfaces through which users can seamlessly interact with the application, empowering them to efficiently manage and monitor their crops with ease.

By harnessing the power of Flutter and strategically capitalizing on the abundant screen real estate of desktop devices, the client-side application offers an unparalleled user experience. It embodies the perfect blend of cross-platform compatibility and intuitive design, elevating agricultural management to new heights and empowering users with the tools they need to maximize productivity and optimize crop yield.

*   Add Farm
*   Monitor Farm

### Add Farm Page

![Add farm](https://raw.githubusercontent.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter/main/img_asset/map.png)

#### Usage

To seamlessly integrate new fields into the system, users can conveniently utilize the intuitive Add Farm page, where they are presented with a comprehensive map interface. Within this interface, users have the ability to precisely define the boundaries of the field by plotting markers that outline its periphery. By placing these markers at strategic locations, users can accurately demarcate the entire field area.

Once all the boundary markers have been meticulously positioned, users can leverage the intuitive "Draw" button to effortlessly calculate the total area covered by the markers on the map. This feature enables users to verify and validate the accuracy of the defined field boundary. 

Furthermore, users have the freedom to assign a customized name or label to the newly added field, providing flexibility and personalization. The system then seamlessly integrates this information into the database by simply clicking the "Save" button, ensuring the proper storage and management of field-related data.

On the server side, a sophisticated grid script adeptly processes the marker plots provided by the user. Employing graph theory algorithms, the script partitions the entire farm into multiple grids of equal size. These grids act as pivotal reference points, serving as navigational guides for the drone as it traverses the vast expanse of the farm. This strategic division of the farm into grids enhances the efficiency and precision of the drone's operations, optimizing data collection and monitoring processes.

Moreover, users are afforded the flexibility to add multiple farms within the system. The Monitor Farm page offers a range of controls and functionalities, enabling users to effortlessly deploy or redeploy the drone to different fields with a few simple clicks. This streamlined and user-friendly approach enhances operational efficiency, allowing users to efficiently manage and monitor their farms with ease.

By seamlessly incorporating new fields, leveraging intelligent grid-based navigation, and providing a user-friendly interface, the system empowers users to effortlessly expand their agricultural operations while maintaining optimal control and oversight over their farms.

### Monitor Farm Page

Once the user selects the specific farm for drone deployment, they gain access to a comprehensive array of controls and drone statistics. The user interface presents a range of meticulously designed controls, empowering the user with seamless command over the drone's operations. These controls encompass three main functionalities:-

*   Deploy Drone:
    
    Utilizing this intuitive button, users can seamlessly deploy the drone within the currently opened farm, initiating an efficient data gathering process with precision and ease.

*   Stall Drone:
   
    Upon deploying the drone, a stall button functionality is incorporated, empowering users to halt the drone at specified positions. This feature facilitates a detailed examination of the images captured by the drone, enabling users to closely analyze the agricultural landscape. Furthermore, manual controls are made available, granting users the ability to exert direct control over the drone's movements through the utilization of the primary drone controller. This comprehensive functionality enhances user engagement and offers a seamless experience in maneuvering the drone for precise observation and analysis.

*   Abort Drone:
   
    The "Abort Drone" button initiates an immediate cessation of the drone's ongoing flight plan, directing it to return promptly to the designated charging dock. This functionality serves to ensure a swift and secure retrieval of the drone, enabling subsequent redeployment if deemed necessary.

![Drone Stats](https://raw.githubusercontent.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter/main/img_asset/drone_stat.png)

The comprehensive top control panel depicted in the figure above provides users with a holistic view of the drone's status and crucial farm-related information. This centralized interface serves as a valuable resource for monitoring and managing the drone's operations in real-time.

Within the control panel, users can readily access pertinent data, including the current altitude of the drone, measured in feet or meters, ensuring precise monitoring of its positioning. The speed of the blades, presented in revolutions per minute (RPM), allows users to gauge the propulsion efficiency and overall performance of the drone.

To ensure uninterrupted drone operations, the control panel displays essential battery statistics, providing users with insights into the current battery level and estimated remaining flight time. This information enables proactive planning and prevents unexpected interruptions during critical farm monitoring activities. 

Moreover, the control panel showcases the current grid identifier of the farm, streamlining the identification and tracking of specific farm areas. Users can easily navigate and focus on different sections of the farm using this reference point. 

Crucial to the agricultural monitoring process, the control panel also presents the diseased percentage of the field, offering a comprehensive assessment of the crop's health status. This valuable metric aids in identifying potential disease outbreaks and facilitates timely intervention to mitigate crop losses. 

Additionally, the total coverage rate, another key metric displayed on the control panel, indicates the extent to which the farm has been surveyed by the drone. This information helps users track the progress of data collection and ensures comprehensive coverage of the entire farm area. 

In addition to the above features, the control panel offers additional functionalities, such as the ability to delete farms that are no longer in operation and the option to rename existing farms. These features enhance the flexibility and customization capabilities of the system, empowering users to adapt and manage their farm portfolios efficiently. 

By providing a comprehensive array of real-time information and valuable functionalities, the top control panel exemplifies the project's commitment to empowering users with a sophisticated and intuitive interface for seamless drone management and optimized farm monitoring.

## Flask Web API

The Flask API is hosted on an Azure virtual machine (VM) that incorporates a local SQL Server deployment. This configuration enables the Flask API to establish a robust data pipeline between the drone and the Farm database. By leveraging the local SQL Server, the Flask API serves as a central hub for data integration and synchronization.

The various routes exposed by the Flask API play a pivotal role in facilitating data entry points for the SQL Server. These routes are meticulously designed to ensure a consistent state is maintained, even in scenarios where multiple drones attempt to update the same database concurrently. To mitigate potential issues such as dirty reads or lost updates, the system employs advanced locking mechanisms during data insertions. This approach guarantees data integrity and enables seamless collaboration among multiple drone units.

Through this well-engineered architecture, the system achieves a high level of reliability, scalability, and data consistency. The Azure VM, coupled with the local SQL Server deployment, provides a robust foundation for data management, while the Flask API acts as a secure and efficient interface, ensuring smooth data flow and synchronization between the drone and the Farm database.

The drone establishes a vital connection with the Flask API to retrieve essential data pertaining to the farms. Simultaneously, the drone also updates the relevant data to the same Flask API, thereby establishing a centralized dependency. While this architecture introduces a central dependency factor, it is important to note that for applications such as crop monitoring, the workload generated is not expected to be significantly intensive, mitigating the likelihood of encountering substantial issues.

To ensure the robustness and scalability of the system, further enhancements can be implemented within the Flask API. By incorporating mechanisms for horizontal scaling, the API can effortlessly handle increased loads as the demand grows. Additionally, introducing a replicated state architecture enables the API to maintain a redundant and synchronized data state across multiple instances. This approach ensures minimal downtime and enhances the overall availability and reliability of the system.

By proactively addressing potential scalability concerns and implementing redundancy measures, the Flask API becomes well-equipped to handle evolving requirements and fluctuations in workload. Consequently, it guarantees optimal performance, seamless data retrieval and update processes, and minimal disruptions in critical functionalities, thereby bolstering the effectiveness and reliability of the crop monitoring application.

## 3D Simulator

![Demo img](https://raw.githubusercontent.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter/main/img_asset/Screenshot%202023-05-11%20at%201.03.56%20AM.png)

The simulator offers intuitive control mechanisms through the utilization of manual controls directly integrated within the system. The user can effortlessly navigate and manipulate the simulator using the "AWSD keys" on their input device. This user-friendly approach enhances the overall user experience, enabling seamless interaction with the simulated environment.

To further enhance the immersive nature of the farm simulation, a variety of 3D objects have been meticulously incorporated. These objects, such as wooden barrels, metal tanks, and wooden boxes, contribute to the realism and authenticity of the virtual agricultural setting. Their presence within the simulated farm environment adds depth and visual appeal, creating a more engaging and captivating experience for users.

Moreover, the simulator screen features a comprehensive user interface (UI) that displays real-time drone statistics. These UI elements provide essential information regarding the drone's performance, including vital metrics such as altitude, speed, battery status, and other relevant parameters. By presenting this data in a clear and accessible manner, users can effectively monitor and analyze the drone's operational characteristics, enabling them to make informed decisions and optimize their farming practices accordingly.

The thoughtful integration of manual controls, immersive 3D objects, and real-time UI elements in the simulator exemplifies the project's commitment to delivering a professional-grade, interactive solution. This cohesive blend of functionality and visual aesthetics creates a compelling virtual environment that closely mirrors real-world farming scenarios, elevating the overall user experience and promoting a deeper understanding of agricultural operations.

![Camera img](https://raw.githubusercontent.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter/main/img_asset/Screenshot%202023-05-11%20at%201.04.40%20AM.png)

In addition, the simulator incorporates a visually informative representation of the camera feed captured by the drone, elegantly displayed in the top left section. This live camera feed plays a pivotal role as it serves as the input to the deployed CNN model for the purpose of obtaining accurate classification results. By leveraging this real-time feed, the system enables prompt and efficient disease detection within the agricultural crops.

Moreover, the simulator goes above and beyond in terms of visual fidelity by incorporating meticulously designed crop models. These models are meticulously textured, portraying two distinct types: diseased texture models and healthy texture models. This attention to detail allows for a visually immersive experience, aiding in the identification and differentiation of diseased and healthy crops within the simulated environment.

To further enhance the realistic ambiance, the terrain within the simulator is thoughtfully crafted with additional aesthetic features. This includes simulated water erosion patterns, seamlessly integrated into the virtual landscape, adding a touch of authenticity. Furthermore, strategically placed high bump textures on the terrain contribute to a more lifelike representation, providing a visually engaging and immersive experience for users.

The integration of these visual and aesthetic elements not only elevates the overall realism of the simulator but also enhances the user's ability to accurately assess and comprehend the condition of the crops. By leveraging advanced graphical techniques and attention to detail, the simulator aims to deliver an immersive and informative environment for users, facilitating effective decision-making processes and promoting a deeper understanding of the agricultural landscape.

![abort statison](https://raw.githubusercontent.com/jashanpreet-singh-99/Drone_crop_monitoring_flutter/main/img_asset/Screenshot%202023-05-11%20at%201.05.24%20AM.png)
