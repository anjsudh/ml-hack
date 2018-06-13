import React from 'react';
import DiseaseList from "./disease-list";


class DiseasePredictor extends React.Component {

  render() {
    return (
      <div className="right-side">
        <div className="header">Probable Diseases</div>
        <DiseaseList diseaseList = {this.props.diseases} save ={this.props.save}/>
      </div>
  );
  }

}

export default DiseasePredictor;
