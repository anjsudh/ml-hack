import React from 'react';
import Symptom from "./symptom";


class SymptomsList extends React.Component {

  render() {
    return (
      <ul>
        {this.props.symptoms.map(symptom => {return <Symptom key={symptom} symptom={symptom} changeHandler={this.props.changeHandler}/>})}
      </ul>)
  }
}

export default SymptomsList;
