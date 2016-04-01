#include "TotemAlignment/RPTrackBased/interface/AlignmentTask.h"
#include "TotemAlignment/RPTrackBased/interface/AlignmentConstraint.h"
#include "TotemAlignment/RPTrackBased/interface/AlignmentGeometry.h"
#include "TotemAlignment/RPTrackBased/interface/LocalTrackFitter.h"

#include <TVectorD.h>
#include <TGraph.h>
#include <TH1D.h>

namespace {
  namespace {
    AlignmentTask at;

    AlignmentConstraint ac;
	std::map<unsigned int, TVectorD> muitvd;

	std::vector<AlignmentConstraint> vac;

	DetGeometry dg;
    AlignmentGeometry ag;

	std::map<unsigned int, DetGeometry> muidg;
	std::set<unsigned int> sui;

    LocalTrackFitter ltf;
	

  }
}
