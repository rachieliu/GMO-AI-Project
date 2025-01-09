import React, { useState } from 'react';

const ConversationForm = () => {
  // State variables for user details
  const [firstName, setFirstName] = useState(''); // First Name
  const [lastName, setLastName] = useState(''); // Last Name
  const [decision, setDecision] = useState(''); // User's Decision
  const [contactValuePhone, setContactValuePhone] = useState(''); // Phone number value
  const [contactValueEmail, setContactValueEmail] = useState(''); // Email value
  const [textInput, setTextInput] = useState(''); // Conversation Text
  const [formData, setFormData] = useState(null); // Holds response data

  // Handle changes for each input field
  const handleFirstNameChange = (e) => setFirstName(e.target.value);
  const handleLastNameChange = (e) => setLastName(e.target.value);
  const handleDecisionChange = (e) => setDecision(e.target.value);
  const handlePhoneChange = (e) => setContactValuePhone(e.target.value);
  const handleEmailChange = (e) => setContactValueEmail(e.target.value);
  const handleTextChange = (e) => setTextInput(e.target.value);

  // Form submission handler
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent page reload on form submission
    console.log('Form submitted');
    console.log('Form data:', {
      firstName,
      lastName,
      decision,
      contactValuePhone,
      contactValueEmail,
      textInput,
    });

    // Constructing the form data as a JSON object
    const formData = {
      firstName,
      lastName,
      decision,
      contactValuePhone,
      contactValueEmail,
      textInput,
    };

    try {
      // Sending POST request to the backend with JSON data
      const response = await fetch('http://localhost:5001/submit-conversation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', // Set content-type to JSON
        },
        body: JSON.stringify(formData), // Send the form data as JSON
      });

      if (!response.ok) {
        throw new Error('Failed to submit conversation');
      }

      // Process the response and update the state
      const result = await response.json();
      console.log('Response from backend:', result);
      setFormData(result); // Update state with the response data
    } catch (error) {
      console.error('Error submitting the form:', error);
    }
  };

  return (
    <div>
      <h3>Connect With a Volunteer</h3>
      <form onSubmit={handleSubmit}>
        {/* User Details Section */}
        <div className="userInfo-section">
          <label>First Name</label>
          <input
            type="text"
            value={firstName}
            onChange={handleFirstNameChange}
            placeholder="Enter your first name"
            required
          />
        </div>
        <div className="userInfo-section">
          <label>Last Name</label>
          <input
            type="text"
            value={lastName}
            onChange={handleLastNameChange}
            placeholder="Enter your last name"
            required
          />
        </div>
        
        {/* Decision Section - Dropdown Selection */}
        <div className="userInfo-section">
          <label>Decision</label>
          <select value={decision} onChange={handleDecisionChange} required>
            <option value="">Select Decision</option>
            <option value="Christian - grow in my faith">Christian - grow in my faith</option>
            <option value="I am not sure about Jesus">I am not sure about Jesus</option>
            <option value="I just decided to follow Jesus">I just decided to follow Jesus</option>
            <option value="I do not want to follow Jesus">I do not want to follow Jesus</option>
            <option value="I want to come back to Jesus">I want to come back to Jesus</option>
          </select>
        </div>

        {/* Conversation Section */}
        <div className="spaced-section">
          <label style={{ marginBottom: '10px', display: 'block' }}>Tell our volunteer what you would like to chat about</label>
          <textarea
            value={textInput}
            onChange={handleTextChange}
            placeholder=""
            rows="5"
            cols="50"
          />
        </div>

        {/* Phone Number Input */}
        <div className="userInfo-section">
          <label>Phone Number</label>
          <input
            type="tel"
            value={contactValuePhone}
            onChange={handlePhoneChange}
            placeholder="Enter your phone number"
            required
          />
        </div>

        {/* Submit Button */}
        <button type="submit" style={{ marginTop: '20px' }}>Submit</button>
      </form>

      {/* Display the processed data if available */}
      {formData && (
        <div>
          <h3>Processed Data</h3>
          <p>Topic: {formData.analysis}</p>
          <p>Language: {formData.language}</p>
          <p>Region: {formData.region}</p>
        </div>
      )}
    </div>
  );
};

export default ConversationForm;
