#
# Compare LLM responses and calculate ROUGE scores
# 2024.05.10
# Christian Jackson

## Example code for calulating rouge score
## https://pypi.org/project/rouge-score/
## https://thepythoncode.com/article/calculate-rouge-score-in-python

## must first install rouge_score
## pip install rouge_score


# Create ists/arrays to store the LLM responses to be compared

# contains the responses from Llama2 before fine tuning
untuned = []

# contains responses from Llama2 after fine tuning on the privacy_policy dataset from huggingface
tuned = []

# contains succinct reponses from GPT4
gpt4 = []

## q1 prompt = "What types of personal data are collected according to this policy: " + policy

untuned.append(
    """
According to the Privacy Policy provided, TopHive collects the following types of personal data:
1. Device Information: TopHive collects information about the device you use to access the website, including the web browser, IP address, time zone, and installed cookies.
2. Personal data provided during registration: TopHive collects personal data such as name, address, company, email address, etc. when you register on the website.
The reasons why TopHive processes your data include:
1. To maintain the website: TopHive processes your data only to the extent necessary to maintain the website and ensure its proper functioning.
2. For marketing activities: TopHive uses the automatically collected information to identify users for marketing activities.
You can visit the website without providing any personal data, but you may not be able to take advantage of some of its features, such as receiving the newsletter or contacting the website directly, if you choose not to provide your personal data.
"""
)

tuned.append(
    """
According to the TopHive website, the following types of personal data are collected:
1. Device Information: This includes information about your device, such as your web browser, IP address, time zone, and installed cookies.
2. Personal Information: This includes information you provide to us during registration, such as your name, address, company, email address, etc.
3. Information collected automatically: This includes information about the individual web pages or products you view, the websites or search terms that referred you to the Site, and how you interact with the Site.
4. Personal data you provide to us: This includes information you provide to us through forms, such as your email, name, last name, city of residence, organization, telephone number.
5. Information you provide to us through the newsletter: This includes information you provide to us through the newsletter, such as your email, name, last name, city of residence, organization, telephone number.
6. Information you provide to us through contact forms: This includes information you provide to us through contact forms, such as your email, name, last name, city of residence, organization, telephone number.
7. Information you provide to us through the website: This includes information you provide to us through the website, such as your email, name, last name, city of residence, organization, telephone number.
8. Information you provide to us through the newsletter: This includes information you provide to us through the newsletter, such as your email, name, last name, city of residence, organization, telephone number.
9. Information you provide to us through the website: This includes information you provide to us through the website, such as your email, name, last name, city of residence, organization, telephone number.
10. Information you provide to us through the newsletter: This includes information you provide to us through the newsletter, such as your email, name, last name, city of residence, organization, telephone number.
11. Information you provide to us through the website: This includes information you provide to us through the website, such as your email, name, last name, city of residence, organization, telephone number.
12. Information you provide to us through the newsletter: This includes information you provide to us through the newsletter, such as your email, name, last name, city of residence, organization, telephone
"""
)

gpt4.append(
    """
The types of personal data collected by TopHive according to their policy include:
Device Information: This automatically collected data includes details about your device, such as your web browser, IP address, time zone, and the cookies installed on your device. It also includes information on the web pages you view on the site, your navigation paths within the site, the websites or search terms that referred you to the site, and your interactions with the site.
Personal Data Provided by Users: This includes data you voluntarily provide during registration or other interactions, such as your name, address, company, email address, last name, city of residence, organization, and telephone number.
"""
)


## q2 prompt = "Does this policy address data sharing with third parties: " + policy

untuned.append(
    """
Yes, this policy addresses data sharing with third parties. Here are the relevant details:
* "We take care of your personal data and undertake to guarantee its confidentiality and security." This suggests that TopHive will take appropriate measures to protect your personal data from unauthorized access or disclosure.
* "Information collected automatically is used only to identify users for marketing activities." This implies that TopHive may share your personal data with third-party marketing partners or use it for marketing purposes itself, but it does not provide any details on how or to whom this data will be shared.
* "You can choose not to provide us with your personal data, but then you may not be able to take advantage of some of the website’s features." This suggests that TopHive may share your personal data with third parties if you choose not to provide it, but it does not provide any details on which features will be unavailable.
Overall, while the policy does address data sharing with third parties, it does not provide much detail on how or to whom this data will be shared, which may be a concern for some users. It is recommended that users who are uncertain about how their data will be used or shared contact TopHive directly for more information.
"""
)

tuned.append(
    """Yes, this policy addresses data sharing with third parties. According to the policy, TopHive may share your personal data with third parties for marketing activities."""
)

gpt4.append(
    """The provided policy does not explicitly state whether TopHive shares personal data with third parties. It focuses on the types of personal information collected, the reasons for its collection, and the commitment to data security and confidentiality, but it does not address data sharing practices with third parties directly."""
)

## q3 prompt = "How does this company share user data with third parties according to this policy?" + policy

untuned.append(
    """
According to the policy, TopHive shares user data with third parties for the following reasons:
1. Marketing activities: TopHive may process only minimal user data, only as much as it is absolutely necessary to maintain the website. Information collected automatically is used only to identify users for marketing activities.
2. Newsletter: If you provide personal data such as your email, name, last name, city of residence, organization, and telephone number, TopHive may share your data with third-party newsletter providers to send you the newsletter.
3. Contact: If you contact TopHive directly from the website, your personal data may be shared with third-party providers to respond to your inquiry.
It's worth noting that TopHive takes care of your personal data and undertakes to guarantee its confidentiality and security. However, since the policy does not provide a comprehensive list of third parties that TopHive may share user data with, it's difficult to determine the exact third parties involved. It's important to review the privacy policy periodically for updates on how TopHive shares user data with third parties.
"""
)

tuned.append(
    """
TopHive shares user data with third parties for the following purposes:
1. Marketing activities: TopHive may share user data with third parties for marketing activities.
2. Legal obligations: TopHive may share user data with third parties to comply with legal obligations.
3. Protection of the rights of others: TopHive may share user data with third parties to protect the rights of others, including intellectual property rights, or to prevent harm to others.
4. Business transfers: In the event that TopHive sells or transfers all or a portion of its business or assets, user data may be one of the transferred assets.
5. Aggregated or de-identified data: TopHive may share aggregated or de-identified data with third parties for various purposes, including research, analysis, and marketing.
6. Service providers: TopHive may share user data with service providers that help us to operate the website, such as payment processors, email providers, and website hosting providers.
7. Government agencies: TopHive may share user data with government agencies or other organizations as required by law or to comply with legal process.
8. Enforcement of our terms of use: TopHive may share user data with third parties to enforce our terms of use or to protect our or other users' rights.
9. Protection of TopHive and others: TopHive may share user data with third parties to protect the rights, property, or safety of TopHive, its users, or others.
10. Other purposes: TopHive may share user data with third parties for other purposes, such as to provide you with special offers or promotions.
"""
)

gpt4.append(
    """
TopHive shares user data with third parties primarily for marketing activities. They collect both automatically generated device information and personal data provided by users. This information is used to identify users for marketing purposes, suggesting that third parties involved are likely those who assist in or benefit from marketing and advertising efforts. The privacy policy does not explicitly list the third parties but indicates the use of user data for these activities.
"""
)


gpt4.append(
    """
TopHive shares user data with third parties primarily for marketing activities. They collect both automatically generated device information and personal data provided by users. This information is used to identify users for marketing purposes, suggesting that third parties involved are likely those who assist in or benefit from marketing and advertising efforts. The privacy policy does not explicitly list the third parties but indicates the use of user data for these activities.
"""
)


## q4 prompt = "How does this company collect data according to this policy: " + policy

untuned.append(
    """
According to this policy, TopHive collects the following personal data from users of its website:
1. Device information: TopHive collects information about the device used to access the website, including the web browser, IP address, time zone, and installed cookies.
2. Page view information: TopHive collects information about the individual web pages or products viewed on the site, as well as the websites or search terms that referred users to the site.
3. Form submissions: TopHive collects personal data provided by users through forms, such as the newsletter sign-up form or contact form. This data may include email address, name, last name, city of residence, organization, and telephone number.
TopHive processes this data for the following purposes:
1. Security: TopHive takes care of the personal data and undertakes to guarantee its confidentiality and security.
2. Marketing activities: TopHive may process only minimal user data, only as much as it is absolutely necessary to maintain the website. Information collected automatically is used only to identify users for marketing activities.
Users can visit the website without providing any personal data, but they may not be able to take advantage of some of the website's features, such as receiving the newsletter or contacting TopHive directly. Users who are uncertain about what information is mandatory can contact TopHive via privacy@tophive.ai.
"""
)

tuned.append(
    """
According to the policy, TopHive collects the following information:
1. Device Information: TopHive collects information about your device, including your web browser, IP address, time zone, and installed cookies.
2. Personal Information: TopHive collects personal information you provide during registration, including your name, address, company, email address, etc.
TopHive processes this data for the following reasons:
1. To maintain the website: TopHive collects information about your device to ensure the website works properly.
2. For marketing activities: TopHive collects information about you to send you a newsletter or other marketing materials.
You can visit the website without providing personal information, but you may not be able to take advantage of some of the website's features if you choose not to provide personal information. 
"""
)

gpt4.append(
    """
TopHive collects data in the following ways according to their Privacy Policy:
Automatically Collected Device Information: When you visit the TopHive website, they automatically gather information about your device, such as your web browser, IP address, time zone, and cookies installed on your device. They also collect data on the web pages you view, the websites or search terms that brought you to the site, and your interactions with the site.
Information You Provide: This includes personal data that you voluntarily provide during registration or other interactions, such as your name, address, email address, company name, city of residence, organization, and telephone number. This type of data is collected when you fill out forms, register for services, or subscribe to newsletters.
The purpose of processing this data includes ensuring the security and functionality of their website and conducting marketing activities. Users have the option to visit the site anonymously, but certain features may not be available without providing personal data.
"""
)

## q5 prompt = "How can I opt out of data collection or marketing according to this policy: " + policy

untuned.append(
    """
According to the policy provided, you can opt out of data collection and marketing activities by:
1. Visiting the website without providing any personal information: You can visit the website without telling us who you are or revealing any information that could identify you as a specific individual.
2. Not providing personal data: If you wish to use some of the website's features or receive the newsletter, you may provide personal data such as your email, name, last name, city of residence, organization, and telephone number. However, if you choose not to provide this information, you may not be able to take advantage of some of the website's features.
3. Contacting the website directly: If you are uncertain about what information is mandatory, you can contact the website directly via privacy@tophive.ai.
By opting out of data collection and marketing activities, you can limit the amount of personal data that is collected and used by TopHive. However, it is important to note that some features of the website may not be available if you choose to opt out of data collection and marketing activities.
"""
)

tuned.append(
    """According to the TopHive website, you can opt out of data collection or marketing by contacting privacy@tophive.ai. """
)

gpt4.append(
    """
To opt out of data collection or marketing at TopHive, you can:
Avoid Providing Personal Data: You do not have to provide personal data to browse the site. By not providing personal data, you can avoid certain features like newsletters or direct contact forms, which may reduce your exposure to marketing.
Contact Privacy Support: Reach out to TopHive through their privacy support email at privacy@tophive.ai. You can inquire about specific data usage and request the deletion or discontinuation of your data use for marketing purposes.
Adjust Your Browser Settings: Control the collection of certain device-related data by adjusting your web browser’s privacy settings to limit cookie tracking and disable location sharing.
Review and Modify Data Consent: When filling out forms or registering on the website, carefully review the consent clauses and opt out of any data sharing or marketing options if provided.
"""
)


## q6 prompt = "How often is this policy reviewed and updated: " + policy

untuned.append(
    """
The Privacy Policy on the TopHive website is reviewed and updated regularly to ensure that it remains current and compliant with relevant data protection laws and regulations. The exact frequency of review and update is not specified in the policy, but it is likely to be at least annually or whenever there are significant changes to the way personal data is collected, processed, or used by TopHive.
It is important to note that the Privacy Policy is a living document that may be updated at any time, and users are encouraged to review it periodically to stay informed of any changes. If you have any questions or concerns about the Privacy Policy or data protection practices of TopHive, you can contact the data protection officer (DPO) or privacy team via the contact information provided in the policy.
"""
)

tuned.append(
    """This policy is reviewed and updated on a regular basis, at least once a year or whenever there is a material change to the way we handle personal information. """
)

gpt4.append(
    """The policy does not specify how frequently it is reviewed and updated. For such details, you should contact the administrators of the TopHive website or refer to any section within the policy that might discuss its revision schedule, if available."""
)


## q7 prompt = "How does this policy cover the use of cookies: " + policy

untuned.append(
    """
This policy covers the use of cookies on the TopHive website. Here are the key points:
1. Automatically collected information: TopHive collects information about your device, including your web browser, IP address, time zone, and installed cookies, when you visit the website. This information is referred to as "Device Information." Additionally, TopHive collects information about the individual web pages or products you view, the websites or search terms that referred you to the site, and how you interact with the site.
2. Personal data: TopHive may collect personal data from you during registration, such as your name, address, company, and email address. This data is used to fulfill the agreement and is processed only as much as it is absolutely necessary to maintain the website.
3. Purpose of processing: TopHive processes your data to maintain the website, provide you with features, and send you a newsletter. You can choose not to provide personal data, but you may not be able to take advantage of some of the website's features.
4. Cookies: TopHive uses cookies to collect information about your browsing behavior and to personalize your experience on the website. You can choose to opt-out of cookie usage by adjusting your browser settings.
5. Data security: TopHive takes care of your personal data and undertakes to guarantee its confidentiality and security.
6. Contact: If you have any questions or concerns about the policy or the use of your personal data, you can contact TopHive via privacy@tophive.ai.
"""
)

tuned.append(
    """This policy covers the use of cookies on the TopHive website. TopHive is the data controller of your personal data.   We have adopted this Privacy Policy, which determines how we are processing the information collected by TopHive, and also provides the reasons why we must collect certain personal data of you. Therefore, you must read this Privacy Policy before using TopHive website.   We take care of your personal data and undertake to guarantee its confidentiality and security.   PERSONAL INFORMATION WE COLLECT:   When you visit TopHive, we automatically collect certain information about your device, including your web browser, IP address, time zone, and some of the installed cookies on your device. Additionally, as you browse the Site, we collect information about the individual web pages or products you view, what websites or search terms referred you to the Site, and how you interact with the Site. We refer to this automatically collected information as “Device Information.” Moreover, we might collect the personal data you provide to us (including, but not limited to, Name, Address, Company, Email Address etc.) during registration to fulfill the agreement.   Why do we process your data?   Our top priority is customer data security and as such, we may process only minimal user data, only as much as it is absolutely necessary to maintain the website. Information collected automatically is used only to identify users for marketing activities.   You can visit the website without telling us who you are or revealing any information by which someone could identify you as a specific, identifiable individual. If, however, you wish to use some of the website’s features, or you wish to receive our newsletter or provide other details by filling out a form, you may provide personal data to us, such as your email, name, last name, city of residence, organization, telephone number. You can choose not to provide us with your personal data, but then you may not be able to take advantage of some of the website’s features. For example, you won’t be able to receive our Newsletter or contact us directly from the website. Users who are uncertain about what information is mandatory are welcome to contact us via privacy@tophive.ai """
)

gpt4.append(
    """
This privacy policy outlines TopHive's data collection and use practices. It describes how TopHive collects both "Device Information" and personal data directly from users. Device Information is collected automatically when a user visits the website and includes data like browser type, IP address, and time zone. Personal data is collected when users voluntarily provide it during processes like registration or filling out forms. This personal data can include names, addresses, email addresses, and other contact information.
The policy explains that data collection is primarily for website maintenance and marketing activities. It also emphasizes data security and confidentiality as a top priority for TopHive.
Users have the option not to provide personal data, but this may limit their ability to use certain website features, such as receiving newsletters or contacting TopHive directly. The policy assures users that they can access the website anonymously without compromising their identity.
For questions about mandatory information and data usage, users are encouraged to contact TopHive through a provided email address.
"""
)


## q8 prompt = "Does this policy describe the use of third party services: " + policy

untuned.append(
    """
Yes, this policy describes the use of third-party services. Here are the relevant details:
1. Device Information: The policy mentions that TopHive collects information about the user's device, including the web browser, IP address, time zone, and installed cookies. This information is automatically collected by TopHive.
2. Personal Data: The policy states that TopHive collects personal data from users during registration, including name, address, company, email address, etc.
3. Processing of Data: The policy explains that TopHive processes only minimal user data, only as much as it is absolutely necessary to maintain the website. The automatically collected information is used only for identifying users for marketing activities.
4. Choice: The policy provides users with the option to choose not to provide personal data, but then they may not be able to take advantage of some of the website's features, such as receiving the newsletter or contacting TopHive directly from the website.
5. Contact: Users who are uncertain about what information is mandatory can contact TopHive via privacy@tophive.ai.
In summary, TopHive collects device information and personal data from users during registration, and processes this data only as much as necessary to maintain the website and for marketing activities. Users have the choice to provide or not provide personal data, but may not be able to take advantage of certain website features if they choose not to provide it.
"""
)

tuned.append(
    """Yes, this policy describes the use of third-party services.   The policy states that the company may collect information from third parties, such as social media platforms, and use that information to enhance the user experience. Additionally, the policy states that the company may use third-party services to collect and analyze data about users' use of the website. """
)

gpt4.append(
    """Yes, the provided policy describes the use of third-party services in relation to how TopHive processes and collects personal data. The policy outlines the types of information collected, the purposes for processing the data, and the measures taken to protect and secure user data."""
)


## q9 prompt = "How does this policy govern the use of my data: " + policy

untuned.append(
    """
This policy governs the use of personal data collected by TopHive, a data controller. The policy outlines the information collected by TopHive, why it is collected, and how it is processed.
TopHive collects the following personal data:
* Device information: including web browser, IP address, time zone, and installed cookies.
* Information about individual web pages or products viewed, websites or search terms that referred users to the site, and how users interact with the site.
* Personal data provided during registration, such as name, address, company, email address, etc.
The data is processed to maintain the website, identify users for marketing activities, and provide newsletters or other forms of communication. Users can visit the website without providing personal data, but may not be able to take advantage of certain features.
The policy also provides information on how users can contact TopHive regarding their data, and how they can choose not to provide certain personal data.
Here are the main points of the policy:
* TopHive is a data controller of personal data.
* The policy outlines how TopHive collects, processes, and uses personal data.
* Personal data collected includes device information and information provided during registration.
* The data is processed to maintain the website, identify users for marketing activities, and provide newsletters or other forms of communication.
* Users can visit the website without providing personal data, but may not be able to take advantage of certain features.
* Users can contact TopHive regarding their data and choose not to provide certain personal data.
Overall, the policy explains how TopHive handles personal data and provides users with information on how to control their data.
"""
)

tuned.append(
    """This policy governs the use of your data by TopHive, a data controller of your personal data. TopHive has adopted this Privacy Policy, which determines how we are processing the information collected by TopHive and also provides the reasons why we must collect certain personal data of you. Therefore, you must read this Privacy Policy before using TopHive website. We take care of your personal data and undertake to guarantee its confidentiality and security.   PERSONAL INFORMATION WE COLLECT:   When you visit TopHive, we automatically collect certain information about your device, including your web browser, IP address, time zone, and some of the installed cookies on your device. Additionally, as you browse the Site, we collect information about the individual web pages or products you view, what websites or search terms referred you to the Site, and how you interact with the Site. We refer to this automatically collected information as “Device Information.” Moreover, we might collect the personal data you provide to us (including, but not limited to, Name, Address, Company, Email Address etc.) during registration to fulfill the agreement.   Why do we process your data?   Our top priority is customer data security and as such, we may process only minimal user data, only as much as it is absolutely necessary to maintain the website. Information collected automatically is used only to identify users for marketing activities.   You can visit the website without telling us who you are or revealing any information by which someone could identify you as a specific, identifiable individual. If, however, you wish to use some of the website’s features, or you wish to receive our newsletter or provide other details by filling out a form, you may provide personal data to us, such as your email, name, last name, city of residence, organization, telephone number. You can choose not to provide us with your personal data, but then you may not be able to take advantage of some of the website’s features. For example, you won’t be able to receive our Newsletter or contact us directly from the website. Users who are uncertain about what information is mandatory are welcome to contact us via privacy@tophive.ai """
)

gpt4.append(
    """
This policy outlines how TopHive handles your personal data. It states:
Data Collection: TopHive collects both automatic data (like browser, IP address, cookies) and user-provided data (like name, email) as you use their site.
Purpose of Data Collection: The data is used for maintaining the website, marketing purposes, and providing requested services.
Data Security and Confidentiality: TopHive commits to protecting your data's security and confidentiality.
Voluntary Provision of Data: You can choose to not provide personal data, but this may restrict access to certain features, such as receiving newsletters.
Contact Information: For uncertainties about mandatory data, contact privacy@tophive.ai.
"""
)


## q10 prompt = "Summarize this policy for me: " + policy

untuned.append(
    """
Sure! Here is a summary of the policy:
TopHive is owned by TopHive, a data controller of personal data. They have created this privacy policy to explain how they collect, use, and protect personal data.
Personal Information Collected:
TopHive collects information about your device, including your web browser, IP address, time zone, and installed cookies. They also collect information about the pages you view and how you interact with the website. Additionally, they may collect personal data you provide during registration, such as name, address, company, and email address.
Why Do We Process Your Data?
TopHive processes personal data only as much as it is necessary to maintain the website and only for marketing activities. They do not collect excessive user data.
Your Choices:
You can visit the website without providing personal information, but you may not be able to use some of its features. If you provide personal data, such as your email address, you can choose not to do so, but you may not be able to receive the newsletter or contact them directly from the website.
Contact Information:
If you have any questions or concerns about this privacy policy, you can contact them via privacy@tophive.ai.
"""
)

tuned.append(
    """TopHive is a website owned by TopHive, a data controller of your personal data. They have adopted this Privacy Policy to determine how they collect, use, and protect your personal data.   They collect information about your device, including your web browser, IP address, time zone, and installed cookies. They also collect information about the pages you view and how you interact with the website.   They may collect personal data you provide during registration, such as name, address, company, email address, etc.   They use this information to maintain the website, identify users for marketing activities, and provide you with their newsletter.   You can visit the website without providing personal information, but you may not be able to take advantage of some of the website's features.   If you have any questions or concerns about their privacy policy, you can contact them via privacy@tophive.ai."""
)

gpt4.append(
    """TopHive's Privacy Policy outlines how they handle personal data collected on their website. They collect information both automatically (device information like web browser, IP address, and site interaction) and directly from users (such as name, address, and email) primarily for security, marketing, and to provide website features. Personal data provision is optional, but some site features may be inaccessible without it. TopHive emphasizes data security and minimal data use to maintain site function. Users can contact them for clarifications on required data via privacy@tophive.ai."""
)


## q11 prompt = "How can I opt out of data collection or marketing communications from this policy: " + policy

untuned.append(
    """
To opt out of data collection or marketing communications from TopHive, you can follow these steps:
1. Adjust your browser settings: You can use your browser's privacy settings to block cookies or limit the amount of data that is collected about you. You can also use a browser extension or add-on to block tracking cookies.
2. Use a VPN: A Virtual Private Network (VPN) can help to encrypt your internet traffic and protect your personal data from being collected.
3. Use a browser that prioritizes privacy: There are several browsers available that are designed with privacy in mind, such as Brave, Tor, and DuckDuckGo. These browsers may have features that help to block tracking cookies and limit data collection.
4. Opt out of targeted advertising: Many websites and advertising networks allow you to opt out of targeted advertising. You can usually find these options in the website's privacy policy or through a third-party opt-out tool.
5. Contact TopHive directly: If you want to opt out of marketing communications from TopHive specifically, you can contact them directly via email at privacy@tophive.ai.
It's important to note that opting out of data collection may limit your ability to use certain features or services on the TopHive website. However, by taking these steps, you can help to protect your personal data and limit the amount of information that is collected about you.
"""
)

tuned.append(
    """
You can opt out of data collection and marketing communications from TopHive by following these steps:
1. Access your account settings: Log in to your TopHive account and go to the "Account" section.
2. Update your privacy settings: From the "Account" section, you can update your privacy settings to opt out of data collection and marketing communications.
3. Unsubscribe from marketing emails: If you have already received marketing emails from TopHive, you can unsubscribe from future emails by clicking on the "Unsubscribe" link at the bottom of the email.
4. Contact us: If you have any questions or concerns about your privacy settings or would like to opt out of data collection and marketing communications, please contact us at privacy@tophive.ai.
5. Use your browser's privacy settings: Most web browsers allow you to control the types of cookies that are stored on your device. You can also use your browser's privacy settings to block all cookies or to block only certain types of cookies. Please note that if you block all cookies, you may not be able to access certain features of the website.
6. Use a browser extension: There are several browser extensions available that can help you manage your privacy settings and block cookies. Some popular options include uBlock Origin, Ghostery, and Privacy Badger.
7. Clear your cookies: If you want to completely remove all cookies from your device, you can use your web browser's "Clear Browsing Data" feature. This will remove all cookies from your device, including any that may have been set by TopHive.
8. Use a VPN: A Virtual Private Network (VPN) can help you to protect your privacy by encrypting your internet traffic and hiding your IP address. This can help to prevent websites from tracking your online activities.
9. Use a browser that blocks tracking: Some web browsers, such as Tor, are designed to block tracking by websites. These browsers can help to protect your privacy by blocking cookies and other tracking technologies.
10. Contact your internet service provider: If you are concerned about the types of data that are being collected about you, you may want to contact your internet service provider to ask about their privacy policies and the types of data they collect. They may be able to provide you with more information about the types of data they collect and how they use it.
"""
)

gpt4.append(
    """
To opt out of data collection and marketing communications from TopHive, you can follow these steps:
Contact via Email: Send an email to privacy@tophive.ai expressing your desire to opt out of data collection and any marketing communications. Be specific about which data processing activities you want to opt out of, and which communications you no longer wish to receive.
Adjust Your Account Settings: If you have an account with TopHive, check for options in your account settings that allow you to control the collection and use of your personal data. You may be able to adjust preferences related to marketing communications or deactivate certain features that collect data.
Unsubscribe from Newsletters: If you receive newsletters or promotional emails from TopHive, you can use the unsubscribe link found at the bottom of the email to opt out of future communications.
Use Website Features Anonymously: According to the policy, you can use the website anonymously without revealing personal data that could identify you. If you choose not to provide personal data, note that some features may not be available.
Contact for Clarifications: If you are unsure about what information is mandatory or have specific questions regarding your personal data, contacting TopHive directly at the provided email address is advisable for further clarification and assistance.
"""
)


## q12 prompt = "How can this policy be improved: " + policy

untuned.append(
    """
Here are some potential improvements that could be made to the privacy policy:
1. More detailed explanation of the types of data collected: While the policy mentions that Device Information is collected, it would be helpful to provide more detail on what specifically is collected (e.g. IP address, browser type, time zone). Additionally, it would be helpful to provide more information on the types of personal data collected (e.g. name, email address, company).
2. Clearer explanation of how data is used: The policy states that the collected data is used only to identify users for marketing activities, but it would be helpful to provide more detail on how this is done (e.g. what types of marketing activities, how the data is analyzed).
3. More information on data sharing: The policy mentions that data may be shared with third parties, but it would be helpful to provide more detail on what types of third parties (e.g. advertisers, analytics providers) and why this data is shared.
4. Clarification on data retention: The policy states that data is retained for as long as necessary, but it would be helpful to provide more detail on how long this is typically, and what criteria are used to determine when data is no longer necessary.
5. More information on data security measures: While the policy mentions that data is confidential and secure, it would be helpful to provide more detail on the specific security measures in place to protect data (e.g. encryption, access controls).
6. A clear and conspicuous link to the privacy policy: It would be helpful to provide a clear and conspicuous link to the privacy policy on the website's homepage and throughout the site.
7. A privacy dashboard: Consider creating a privacy dashboard where users can easily access and manage their personal data, and where they can easily find answers to common privacy questions.
8. A clear and simple explanation of data subject rights: Make sure to inform users of their rights, such as the right to access, correct, or delete their personal data, and how they can exercise these rights.
9. A clear and simple explanation of the legal basis for data processing: Make sure to inform users of the legal basis for processing their personal data, and how this basis is related to the purpose of the data processing.
10. A clear and simple explanation of the data controller's contact information: Make sure to provide the data controller's contact information, such as an email address or phone number, where users can reach out with questions or concerns about the privacy policy.
It's also important to keep in mind that privacy policies should be written in a clear and concise manner, using language that is easy for users to understand. It's also important to regularly review and update the privacy policy to ensure it remains accurate and relevant.
"""
)

tuned.append(
    """
Thank you for sharing your feedback on the TopHive website's privacy policy. Here are some suggestions for improvement:
1. Add a clear and concise summary of the policy: It would be helpful to have a brief summary of the policy at the top of the page, so that users can quickly understand what information is being collected and why.
2. Use simpler language: The policy uses technical terms and jargon that may be difficult for some users to understand. Consider using simpler language and providing explanations for technical terms.
3. Provide more information about the types of data collected: While the policy mentions that TopHive collects "Device Information," it would be helpful to provide more information about the types of data that are collected, such as IP addresses, browser types, and device types.
4. Explain how data is used: While the policy mentions that data is used only to identify users for marketing activities, it would be helpful to provide more information about how data is used, such as how it is analyzed and how it is shared with third parties.
5. Provide more information about the security measures in place: While the policy mentions that TopHive takes care of personal data and undertakes to guarantee its confidentiality and security, it would be helpful to provide more information about the security measures in place, such as encryption and access controls.
6. Provide a way for users to access and correct their personal data: It would be helpful to provide a way for users to access and correct their personal data, such as a "My Account" feature.
7. Provide a way for users to opt-out of data collection: While the policy mentions that users can choose not to provide personal data, it would be helpful to provide a way for users to opt-out of data collection altogether.
8. Provide more information about third-party data sharing: While the policy mentions that TopHive may share data with third parties, it would be helpful to provide more information about the types of third parties with which data is shared and how the data is used by those third parties.
9. Provide more information about the retention period of personal data: While the policy mentions that personal data is retained for as long as necessary, it would be helpful to provide more information about the retention period of personal data and how it is determined.
10. Provide more information about the rights of users: While the policy mentions that users have certain rights, such as the right to access and correct their personal data, it would be helpful to provide more information about those rights and how they can be exercised.
I hope these suggestions are helpful in improving the privacy policy of TopHive.
"""
)

gpt4.append(
    """
The policy could be improved for clarity, conciseness, and user understanding in several ways:
Clearer Ownership and Purpose:
Simplify and clarify the opening statement to immediately inform the reader of the purpose of the policy and who it applies to.
Enhanced Readability:
Break down complex sentences into simpler ones.
Use bullet points for lists, such as the types of collected data, to improve readability.
Concise Language:
Reduce redundancy and remove unnecessary clauses that don't add value to the understanding of the policy.
Specific Sections and Headings:
Use distinct headings for different sections like ‘Personal Information We Collect’, ‘Why We Process Your Data’, and ‘Your Rights’ to structure the document better and make it easier to navigate.
Transparent Processing Information:
Specify which types of data are processed automatically and which require explicit consent.
Clarify the use of automatically collected data versus data provided by the user.
Data Security and Confidentiality:
Highlight how personal data is protected and what measures are in place to ensure its security.
User Choices and Rights:
Provide clear options for users regarding how they can manage or withdraw their consent, access the data you have about them, or request data deletion.
Contact Information:
Clearly mention how users can contact you for privacy concerns, preferably at the beginning or end of the document.
Here's a revised version of the policy, incorporating these suggestions:
Privacy Policy
Introduction: Welcome to the TopHive website, owned and operated by TopHive. This Privacy Policy outlines how we handle your personal data to ensure your privacy and security. Please review this policy before using our services.
Data Controller: TopHive is the data controller of your personal data.
Personal Information We Collect:
Automatically Collected Information: When you visit our website, we automatically collect information about your device and interaction with our site. This includes your web browser, IP address, time zone, and some cookies installed on your device.
Information You Provide: This includes any personal details you provide during registration or while using our services, such as your name, address, email, and telephone number.
Purpose of Data Processing: Our primary goal in processing your data is to enhance site security and user experience. Data collected automatically supports our marketing activities and website maintenance. We process minimal personal data, strictly necessary for these purposes.
Your Privacy Rights: You can browse our site without providing personal data. However, some features require personal data to function, such as our newsletter or contact forms. You have the right to access, modify, or delete your information and can manage your preferences at any time.
Data Security: We are committed to protecting your data and maintaining its confidentiality through stringent security measures.
Contact Us: For questions about this policy or your personal data, please contact us at privacy@tophive.ai.
This revision aims to make the policy more accessible and straightforward for users while ensuring all necessary legal information is included.
"""
)

# Import the module
from rouge_score import rouge_scorer

## Calculate ROUGE scores for the untuned Llama27b model compared to GPT4

print("\n\nROUGE scores comparing untuned Llama2-7b vs GPT-4 baseline")
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
for i in range(12):
    print("Question ", i + 1)
    scores = scorer.score(untuned[i], gpt4[i])
    for key in scores:
        print(f"{key}: {scores[key]}")

## Calculate ROUGE scores for the fine-tuned Llama27b model compared to GPT4

print("\n\nROUGE scores comparing fine-tuned Llama2-7b vs GPT-4 baseline")
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
for i in range(12):
    print("Question ", i + 1)
    scores = scorer.score(tuned[i], gpt4[i])
    for key in scores:
        print(f"{key}: {scores[key]}")
