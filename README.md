# 🌟 EC2 Instance Scheduler

This repository contains two AWS Lambda functions designed to automate the starting and stopping of development EC2 instances. These functions are useful for managing costs by ensuring that development instances are only running during working hours.

## 🚀 Features

- **StartDevEC2Function**: This Lambda function starts EC2 instances tagged with `env:dev` at 8:00 AM every day.
- **StopDevEC2Function**: This Lambda function stops EC2 instances tagged with `env:dev` at 6:00 PM every day.

## 📝 Usage

To use these Lambda functions:

1. Deploy the functions to your AWS account.
2. Configure triggers for each function using AWS EventBridge to schedule them to run at the desired times.
3. Ensure that the IAM role attached to the Lambda functions has appropriate permissions to start and stop EC2 instances.

## 🛠️ Setup

Follow these steps to set up and deploy the Lambda functions:

1. Install dependencies (if any) and package the Lambda functions.
2. Deploy the functions to your AWS account using the AWS CLI or AWS Management Console.

## 📅 EventBridge Schedule

You can schedule the Lambda functions to run at specific times using AWS EventBridge.

### StartDevEC2Function Schedule

Schedule this function to run daily at 8:00 AM.

### StopDevEC2Function Schedule

Schedule this function to run daily at 6:00 PM.

## 📚 Documentation

For more information about AWS Lambda, AWS EventBridge, and managing EC2 instances, refer to the AWS documentation:

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda)
- [AWS EventBridge Documentation](https://docs.aws.amazon.com/eventbridge)
- [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2)

## 🤝 Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💰 Cost Savings

Automating the starting and stopping of development EC2 instances using these Lambda functions can lead to significant cost savings by ensuring that instances are only running when necessary.
