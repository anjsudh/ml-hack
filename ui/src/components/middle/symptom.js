import React from 'react';
import MultiToggle from "../common/multi-toggle-button";


class Symptom extends React.Component {

  changeHandler = (value) => {
    this.props.changeHandler(this.props.symptom, value);
  };

  render() {
    return (
      <li className="li symptom-li">
        {this.props.symptom}
        <MultiToggle selected={null} options={[{key: "true", value: " ✔ "}, {key: "false", value: " ✘ "}, {key: null, value: "-"}]} onChange={this.changeHandler}/>
      </li>)
  }
}

export default Symptom;
