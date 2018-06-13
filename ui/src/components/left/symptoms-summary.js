import React from 'react';


class SymptomsSummary extends React.Component {

  render() {
    return (
      <div className="left-side">
        <div className="header">Identified Symptoms</div>
        <div className="header green"> ✔ </div>
          <ul>
          {this.props.positiveSymptoms.map(p => {return (<li key={p} className="li positive-symptom-li">{p}</li>)})}
          </ul>
        <div className="header red"> ✘ </div>
          <ul>
            {this.props.negativeSymptoms.map(p => {return (<li key={p} className="li negative-symptom-li">{p}</li>)})}
          </ul>
      </div>
    );
  }

}

export default SymptomsSummary;
