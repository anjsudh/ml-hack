import React from 'react';
import Disease from "./disease";


class DiseaseList extends React.Component {

  render() {
    return (
      <ul>
        {this.props.diseaseList.map((disease) => {return (<Disease key={disease[0]} disease={disease} save={this.props.save}></Disease>)})}
      </ul>
  );
  }

}

export default DiseaseList;
